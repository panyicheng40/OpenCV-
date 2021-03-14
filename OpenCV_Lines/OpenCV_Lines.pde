import gab.opencv.*;
import processing.video.Capture;

OpenCV opencv;
Capture cam;

int zoom = 1;
int size = 3;
boolean invert = true;

// input resolution
int w = 160 * size, h = 120 * size;
//int w = 1080, h = 720;

void setup() {
  size(480, 360);
  
  // init cam
  cam = new Capture(this, w, h);
  cam.start();
  
  // init opencv
  opencv = new OpenCV(this, w, h);
  
}

color c1 = #ffff00;
color c2 = #ff00ff;
color c3 = #00ffcc;

color[] colorsArr = {c1,c2,c3 };


void draw() {
  
  opencv.loadImage(cam);
  
  scale(zoom);
  
  //webcam image
  PImage src = snapshot("original", 0, 0);
  
  //edges
  opencv.findCannyEdges(120, 75);
  if(invert) opencv.invert();
  snapshot("canny", 0, 0);

}


// read a new frame when it's available
void captureEvent(Capture c) {
  c.read();
}


// create a snapshot and display it
PImage snapshot(String label, int px, int py) {  
  
  // show image
  PImage img = opencv.getSnapshot();
  

  if (label == "canny"){
    img.loadPixels();
    int dimension = img.width * img.height;
    
    for (int i = 0; i < dimension; i += 1) {
      if (img.pixels[i] == -1){ //if the contrasted image color is black(?) make it black transparent
        img.pixels[i] = color(0, 0, 0, 0); 
      } else {
         int randColor = int(random(0,2));
         //img.pixels[i] = colorsArr[randColor]; //random color //MH - how to get connected lines?
         img.pixels[i] = c2; //solid color
      }
    } 
    
    image(img, 0,0);
  } else {
    image(img, 0,0);
  }
  
 
  // image outline
  noFill(); 
  //stroke(invert ? 0 : 255); 
  //rect(px * w, py * h, w, h);
  
  // return the snapshot so we can reuse it
  return img;
}


void keyPressed() {
  invert = !invert; 
}
