package main

import (
	"fmt"
	"log"
	"net"
	"sync"
	"time"
)

func scanPort(portNumber int) bool {
	conn, err := net.Dial("tcp", fmt.Sprintf("localhost:%d", portNumber))
	if err != nil {
		return false
	}
	defer conn.Close()
	return true
}

func main() {
	const MAX_PORT int = 65536
	wg := sync.WaitGroup{}
	outCh := make(chan int)
	totalTime := float64(0)

	log.Println("Starting Port Scan")
	tx := time.Now()

	for port := 1; port < int(MAX_PORT); port++ {
		wg.Add(1)

		// dial the port and report the status
		go func() {
			tx := time.Now()
			if scanPort(port) {
				outCh <- port
			}
			td := time.Since(tx)
			totalTime += td.Seconds()
			wg.Done()
		}()
	}

	// wait for all port scans to complete
	go func() {
		wg.Wait()
		outCh <- -1
	}()

	// this loop will check both channels and stop when the stopCh receives a signal
	for p := range outCh {
		if p == -1 {
			td := time.Since(tx).Seconds()
			avg := totalTime / float64(MAX_PORT)
			log.Printf("!! Scanned %d ports in %f seconds (%f seconds per scan)\n", MAX_PORT, td, avg)
			return
		}
		log.Printf("Open Port: %d", p)
	}
}
