import gab.opencv.*;
import processing.video.*;

Movie mov;
OpenCV cv;

PImage dst;
ArrayList<Contour> contours;
ArrayList<Contour> polygons;
boolean invert = true;

void setup() {
  
  size(1080, 360);

  mov = new Movie(this, "launch.mp4");   
  mov.play();
  mov.jump(0);
  mov.loop();

  cv = new OpenCV(this, mov.width, mov.height);
  
}


void draw() {
  if (mov.available()) {
    mov.read();
    
    // display the frame onscreen
    image(mov, 1080/2, 0, 540, 360);

    // then pass it to OpenCV using get()
    cv = new OpenCV(this, get(1080/2, 0, 540, 360));
    cv.threshold(95);
    dst = cv.getOutput();
    contours = cv.findContours();
    image(dst, 0, 0);
    noFill();
    strokeWeight(3);
    
    for (Contour contour : contours) {
      stroke(0, 255, 0);
      contour.draw();
      
      stroke(255, 0, 0);
      beginShape();
      for (PVector point : contour.getPolygonApproximation().getPoints()) {
        vertex(point.x, point.y);
      }
      endShape();
    }
    

    
  }
}
