package main

import (
	"image"
	"image/color"
	"image/draw"
	"log"
	"sync"
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"

	vlc "github.com/adrg/libvlc-go/v3"
)

// Global variables for the video frame.
var (
	frameMutex  sync.Mutex
	frameBuffer []byte
	frameWidth  int = 640 // desired width
	frameHeight int = 360 // desired height
	videoImg    *canvas.Image
)

// lockCallback provides a pointer to our frame buffer.
func lockCallback(userData interface{}, pPixels **byte) {
	frameMutex.Lock()
	if frameBuffer == nil {
		// Allocate buffer for RGBA (4 bytes per pixel).
		frameBuffer = make([]byte, frameWidth*frameHeight*4)
	}
	*pPixels = &frameBuffer[0]
}

// unlockCallback simply unlocks our frame buffer.
func unlockCallback(userData interface{}, id int, pPixels *byte) {
	frameMutex.Unlock()
}

// displayCallback triggers a UI refresh.
func displayCallback(userData interface{}, id int) {
	// Refresh the Fyne image on the main thread.
	if videoImg != nil {
		videoImg.Refresh()
	}
}

func main() {
	// Initialize libVLC without disabling video.
	if err := vlc.Init("--quiet"); err != nil {
		log.Fatal(err)
	}
	defer vlc.Release()

	// Create a new libVLC player.
	player, err := vlc.NewPlayer()
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		player.Stop()
		player.Release()
	}()

	// Set video callbacks.
	if err := player.SetVideoCallbacks(lockCallback, unlockCallback, displayCallback, nil); err != nil {
		log.Fatal(err)
	}

	// Set the video format to RV32 (RGBA) with our desired dimensions.
	if err := player.SetVideoFormat("RV32", uint32(frameWidth), uint32(frameHeight), uint32(frameWidth*4)); err != nil {
		log.Fatal(err)
	}

	// Create a Fyne application and window.
	a := app.New()
	w := a.NewWindow("Embedded Video Player")

	// Create an initial blank RGBA image.
	img := image.NewRGBA(image.Rect(0, 0, frameWidth, frameHeight))
	draw.Draw(img, img.Bounds(), &image.Uniform{C: color.Black}, image.Point{}, draw.Src)
	videoImg = canvas.NewImageFromImage(img)
	videoImg.FillMode = canvas.ImageFillContain

	w.SetContent(videoImg)
	w.Resize(fyne.NewSize(float32(frameWidth), float32(frameHeight)))
	w.Show()

	// Load media from URL.
	// (Note: Replace this URL with a valid video URL that libVLC can play.)
	media, err := player.LoadMediaFromURL("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
	if err != nil {
		log.Fatal(err)
	}
	defer media.Release()

	// Start playing the media.
	if err := player.Play(); err != nil {
		log.Fatal(err)
	}

	// Launch a goroutine to periodically update the Fyne image from our frame buffer.
	go func() {
		ticker := time.NewTicker(33 * time.Millisecond) // ~30 FPS
		defer ticker.Stop()
		for range ticker.C {
			frameMutex.Lock()
			if frameBuffer != nil {
				// Create an RGBA image using the frame buffer.
				img := &image.RGBA{
					Pix:    frameBuffer,
					Stride: frameWidth * 4,
					Rect:   image.Rect(0, 0, frameWidth, frameHeight),
				}
				videoImg.Image = img
			}
			frameMutex.Unlock()
			videoImg.Refresh()
		}
	}()

	// Run the Fyne application.
	a.Run()

	// Stop the player when the window is closed.
	player.Stop()
}
