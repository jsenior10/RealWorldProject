
function displayInputState(message){
    
    fill(0)
    rect(0,0, 85,20)
    
    if (inputState){
        fill(0,255,0)
    }else{
        fill(255,0,0)
    }
    text(message, 20,15)
}

function displayTimeElapsed(seconds, minutes){
    
    fill(0)
    rect(425,0, 85, 20)
    
    fill(255)
    text(int(minutes), 446, 15)
    text(":", 456, 14)
    
    if (seconds < 10){
        text(0, 461,15)
        text(int(seconds), 468,15)
    }else{
        text(int(seconds), 461, 15)
    }
}

function displayKeys(){
   
    if (keyIsDown(UP_ARROW) && inputState){
        fill(0,255,0) 
    } else {
        fill(255) 
    }
    rect(240,5, 20,10)
    
    if (keyIsDown(DOWN_ARROW) && inputState){
        fill(0,255,0) 
    } else {
        fill(255) 
    }
    rect(240,15, 20, 10)
    
    if (keyIsDown(LEFT_ARROW) && inputState){
        fill(0,255,0) 
    } else {
        fill(255) 
    }
    rect(220,10, 20, 10)
    
    if (keyIsDown(RIGHT_ARROW) && inputState){
        fill(0,255,0) 
    } else {
        fill(255) 
    }
    rect(260,10, 20,10) 
    
}