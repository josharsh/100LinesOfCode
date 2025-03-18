// package main

// import (
// 	"encoding/json"
// 	"io/ioutil"
// 	"log"
// 	"strconv"

// 	"fyne.io/fyne/v2/app"
// 	"fyne.io/fyne/v2/container"
// 	"fyne.io/fyne/v2/widget"
// 	vlc "github.com/adrg/libvlc-go/v3"
// )

// type Question struct {
// 	Q       string   `json:"question"`
// 	Choices []string `json:"choices"`
// 	Answer  int      `json:"answer"`
// }

// func main() {
// 	if err := vlc.Init("--quiet"); err != nil {
// 		log.Fatal(err)
// 	}
// 	defer vlc.Release()
// 	player, err := libvlc.NewPlayer()
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	defer player.Stop()
// 	media, err := player.LoadMedia("sample.mp4")
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	defer media.Release()

// 	data, err := ioutil.ReadFile("questions.json")
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	var questions []Question
// 	if err := json.Unmarshal(data, &questions); err != nil {
// 		log.Fatal(err)
// 	}

// 	a := app.New()
// 	w := a.NewWindow("Video & Exam Dashboard")

// 	playBtn := widget.NewButton("Play", func() { player.Play() })
// 	pauseBtn := widget.NewButton("Pause", func() { player.SetPause(true) })
// 	stopBtn := widget.NewButton("Stop", func() { player.Stop() })
// 	videoTab := container.NewVBox(
// 		widget.NewLabel("Video Controls:"),
// 		playBtn, pauseBtn, stopBtn,
// 		widget.NewLabel("Note: Video output appears in a separate window."),
// 	)

//		score, idx := 0, 0
//		qLabel := widget.NewLabel("")
//		radio := widget.NewRadioGroup([]string{}, nil)
//		resLabel := widget.NewLabel("")
//		var loadQuestion func(int)
//		loadQuestion = func(i int) {
//			qLabel.SetText(questions[i].Q)
//			radio.Options = questions[i].Choices
//			radio.Selected = ""
//			radio.Refresh()
//		}
//		nextBtn := widget.NewButton("Next", func() {
//			if radio.Selected == questions[idx].Choices[questions[idx].Answer] {
//				score++
//			}
//			idx++
//			if idx >= len(questions) {
//				qLabel.SetText("Exam Completed!")
//				radio.Options = nil
//				nextBtn.Disable()
//				resLabel.SetText("Score: " + strconv.Itoa(score) + "/" + strconv.Itoa(len(questions)))
//				return
//			}
//			loadQuestion(idx)
//		})
//		loadQuestion(idx)
//		examTab := container.NewVBox(qLabel, radio, nextBtn, resLabel)
//		tabs := container.NewAppTabs(
//			container.NewTabItem("Video", videoTab),
//			container.NewTabItem("Exam", examTab),
//		)
//		w.SetContent(tabs)
//		w.ShowAndRun()
//	}
package main

import (
	"log"

	vlc "github.com/adrg/libvlc-go/v3"
)

func main() {
	// Initialize libVLC. Additional command line arguments can be passed in
	// to libVLC by specifying them in the Init function.
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

	// Add a media file from path or from URL.
	// Set player media from path:
	// media, err := player.LoadMediaFromPath("localpath/test.mp4")
	// Set player media from URL:
	media, err := player.LoadMediaFromURL("http://stream-uk1.radioparadise.com/mp3-32")
	if err != nil {
		log.Fatal(err)
	}
	defer media.Release()

	// Retrieve player event manager.
	manager, err := player.EventManager()
	if err != nil {
		log.Fatal(err)
	}

	// Register the media end reached event with the event manager.
	quit := make(chan struct{})
	eventCallback := func(event vlc.Event, userData interface{}) {
		close(quit)
	}

	eventID, err := manager.Attach(vlc.MediaPlayerEndReached, eventCallback, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer manager.Detach(eventID)

	// Start playing the media.
	err = player.Play()
	if err != nil {
		log.Fatal(err)
	}

	<-quit
}
