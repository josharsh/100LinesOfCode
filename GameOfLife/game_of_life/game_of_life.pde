GOL game;

void setup(){
  frameRate(10);
  size(800, 600);
  game = new GOL();
}

void draw(){
  background(255);
  game.render();
  game.generate();
}
