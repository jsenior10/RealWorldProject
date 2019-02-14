var message = "Input off"
var inputState = false   
var seconds = 0 
var minutes = 0 

function setup(){
    
    createCanvas(500,400)
    background(51)
    fill(255,0,0);
    test = loadImage("test1.jpg")
}

function draw(){
    
    if (inputState){
         catchKeys();   
    }    

    displayInputState(message);
    secondHandler();
    displayTimeElapsed(seconds,minutes);
    displayKeys();
    
    fill(180)
    rect(10,30, 480, 360)
    
    image(test, 11, 31, 479, 359) // in the future this is the embedded video 
    
}

function secondHandler(){
   
    seconds += 1/60
    if (seconds > 60){
        seconds = 0 
        minutes += 1 
    }
}
