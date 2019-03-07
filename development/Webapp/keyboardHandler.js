
function catchKeys(){
    if (keyIsDown(UP_ARROW)){
        console.log("pressed up") 
    }
    if (keyIsDown(LEFT_ARROW)){
        console.log("pressed left")
    }
    if (keyIsDown(RIGHT_ARROW)){
        console.log("pressed right")
    }
    if (keyIsDown(DOWN_ARROW)){
        console.log("pressed down")
    }
}

function keyPressed(){    
    if (keyCode == ENTER){ 
        console.log("pressed enter")
        if (inputState){
            inputState = false 
            message = "Input off"
        }else{
            inputState = true 
            message = "Input on"   
        }

    }
}