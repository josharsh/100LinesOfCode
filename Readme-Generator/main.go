package main

import (
	"bufio"
	"fmt"
	"os"
)

type Project struct {
	Title        string
	Description  string
	Install      string
	Usage        string
	Dependencies string
	Contributors string
}

func main() {
	var project = Project{}
	fmt.Println("Veuillez entrer les informations du projet :")
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Titre : ")
	scanner.Scan()
	project.Title = scanner.Text()

	fmt.Print("Description : ")
	scanner.Scan()
	project.Description = scanner.Text()

	fmt.Print("Installation : ")
	scanner.Scan()
	project.Install = scanner.Text()

	fmt.Print("Usage : ")
	scanner.Scan()
	project.Usage = scanner.Text()

	fmt.Print("Dépendances : ")
	scanner.Scan()
	project.Dependencies = scanner.Text()

	fmt.Print("Contributeurs : ")
	scanner.Scan()
	project.Contributors = scanner.Text()

	file, err := os.Create("README.md")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	fmt.Fprintf(file, "# %s\n\n", project.Title)
	fmt.Fprintf(file, "%s\n\n", project.Description)
	fmt.Fprintf(file, "## Installation\n\n```bash\n%s\n\n```\n\n\n", project.Install)
	fmt.Fprintf(file, "## Usage \n\n\n%s\n\n", project.Usage)
	fmt.Fprintf(file, "## Dépendances\n\n%s\n\n", project.Dependencies)
	fmt.Fprintf(file, "## Contributeurs\n\n%s\n", project.Contributors)

	fmt.Println("README.md créé avec succès.")
}
