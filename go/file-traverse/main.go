package main

import (
	"path/filepath"
	"os"
	"fmt"
	"strings"
	"time"
)

const source = "" // file path in string
const destination = "" // file path in string
const keyword = "" // keyword in path
const separator = "" // "\\" for windows and "/" for unix/linux

func main() {
	start := time.Now()
	CreateDirIfNotExist(destination)
	err := filepath.Walk(source, visit)

	if err != nil {
		fmt.Printf("filepath.Walk() returned %v\n", err)
	}
	fmt.Printf("Duration: %s\n", time.Since(start))
}

func visit(path string, f os.FileInfo, err error) error {
	if strings.Contains(path, keyword) {
		i, j := strings.LastIndex(path, separator), len(path)
		os.Rename(path, destination + path[i:j])
	}
	return nil
}

func CreateDirIfNotExist(path string) {
	_, err := os.Stat(path)
	if err != nil && os.IsNotExist(err) {
		// folder not exist
		os.Mkdir(path, os.ModeDir)
	}
}
