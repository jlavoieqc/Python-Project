var dinosaurs = ["T-Rex", "Brachiosaurus", "Pterodactyl", "Stegosaurus", "Triceratops"];

var userChoice = prompt("Which dinosaur would you like to learn about? We have T-Rex, Brachiosaurus, Pterodactyl, Stegosaurus, and Triceratops.");

if (userChoice === "T-Rex") {
  console.log("The T-Rex is one of the most popular dinosaurs. It lived during the Cretaceous period and was one of the last non-avian dinosaurs to exist. It was a carnivore and could grow up to 40 feet long and weigh up to 7 tons.");
} else if (userChoice === "Brachiosaurus") {
  console.log("The Brachiosaurus was a large sauropod that lived during the Jurassic period. It was one of the largest land animals ever to exist, with some estimates suggesting it could grow up to 85 feet long and weigh up to 80 tons.");
} else if (userChoice === "Pterodactyl") {
  console.log("The Pterodactyl was a flying reptile that lived during the Jurassic and Cretaceous periods. It was the largest known flying animal of all time, with some estimates suggesting it could have a wingspan of up to 40 feet.");
} else if (userChoice === "Stegosaurus") {
  console.log("The Stegosaurus was a large herbivorous dinosaur that lived during the Jurassic period. It was easily recognizable due to the large plates on its back, which were used for defense against predators.");
} else if (userChoice === "Triceratops") {
  console.log("The Triceratops was a large herbivorous dinosaur that lived during the Cretaceous period. It was easily recognizable due to its three horns and large frill.");
} else {
  console.log("That is not a valid dinosaur. Please try again.");
}