function isSorted(parent, len){
    for(var i = 0; i < parent.childElementCount - 1; i++) {
        console.log(parent.children[i].innerHTML, parent.children[i+1].innerHTML)
        if(parent.children[i].innerHTML > parent.children[i+1].innerHTML) {
            return false;
        }
    }
    return true
}

function checkResult(){
    let mainBox = document.getElementById("wrap")
    let innerC = mainBox.children[1]
    let leftC = innerC.children[0]
    lenOfinitialBox = leftC.childElementCount
    
    let flag = false
    let count = 0


    for(let i = 1; i < 3; i++){
        let box = mainBox.children[i]
        let innerBox= box.children[0]

        let len = innerBox.childElementCount

        if(len == 0) count++

        if(len == lenOfinitialBox && isSorted(innerBox, len)){
            flag = true
            // console.log(true)
            successBox()
            break
        }
    }
    console.log("in here")

    if(count == lenOfinitialBox){
        document.location.reload()
    }
    else if(flag == false){
        loseBox()
    }
}