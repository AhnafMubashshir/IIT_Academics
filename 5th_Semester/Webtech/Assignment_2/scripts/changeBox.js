function changeBox(pBox , dBox){
    let mainBox = document.getElementById("wrap")

    let temp = mainBox.children[pBox]
    let presentBox = temp.children[0]

    temp = mainBox.children[dBox]
    let destinationBox = temp.children[0]


    if(presentBox.children[0] != undefined){
        destinationBox.prepend(presentBox.children[0])
    }
}