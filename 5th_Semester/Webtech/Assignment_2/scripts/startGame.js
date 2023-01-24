function removeAll(){
    let mainDiv = document.getElementById("wrap")

    for(let i = 1; i < 4; i++){
        let box = mainDiv.children[i]
        let innerBox= box.children[0]

        let len = innerBox.childElementCount

        for(let j = 0; j < len; j++){
            innerBox.removeChild(innerBox.children[0])
        }
    }
}


function starGame(){
    let mainDiv = document.getElementById("wrap")
    let box = mainDiv.children[1]
    let innerBox= box.children[0]

    removeAll()
    
    var arr = [];
    while(arr.length < 7){
        var x = Math.floor(Math.random()*7)+1;
        if(arr.indexOf(x) == -1){
            arr.push(x);

            let para = document.createElement("p")
            para.append(x)

            let elem = document.createElement("div")
            elem.classList = "boxDiv"
            elem.append(para)

            innerBox.append(elem)
        }
    }
    console.log(innerBox)
}