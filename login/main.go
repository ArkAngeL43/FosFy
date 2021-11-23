package main

import (
	"flag"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"time"
)

var (
	clear  map[string]func()
	flagSt = flag.String("p", "", `password`)
)

func init() {
	clear = make(map[string]func())
	clear["linux"] = func() {
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
	clear["windows"] = func() {
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
}

func CallClear() {
	value, ok := clear[runtime.GOOS]
	if ok {
		value()
	} else {
		panic("[ - ] this call to clear might not be supported")
	}
}

func main() {
	flag.Parse()
	if *flagSt == "" {
		fmt.Println("[ - ] Key not implimented")
		fmt.Println("[ - ] Usages: -> ./main -p password")
		os.Exit(1)
	}
	if *flagSt == "TTVsasy301" {
		fmt.Println("[ + ] password came back true, loading script")
		time.Sleep(2 * time.Second)
		CallClear()
		os.Exit(1)
	}
}
