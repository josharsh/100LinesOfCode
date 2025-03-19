package main

import (
	"log"
	"os"
	"os/signal"
	"syscall"

	vlc "github.com/adrg/libvlc-go/v3"
)

func main() {
	// Initialize libVLC.
	if err := vlc.Init("--no-video", "--quiet"); err != nil {
		log.Fatal(err)
	}
	defer vlc.Release()

	// Create a new player.
	player, err := vlc.NewPlayer()
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		player.Stop()
		player.Release()
	}()

	// Load media from URL.
	media, err := player.LoadMediaFromURL("http://stream-uk1.radioparadise.com/mp3-32")
	if err != nil {
		log.Fatal(err)
	}
	defer media.Release()

	// Start playing the media.
	if err := player.Play(); err != nil {
		log.Fatal(err)
	}

	log.Println("Streaming... Press Ctrl+C to stop.")

	// Set up signal handling to wait for an interrupt (Ctrl+C).
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, os.Interrupt, syscall.SIGTERM)
	<-sigs

	log.Println("Interrupt received. Stopping playback.")
	player.Stop()
}
