function successBox(){
    var modal = document.getElementById("myModal");

    var div = modal.children[0]
    div.classList = "modal-content"

    var image = document.createElement("img")
    image.classList = "image"
    image.src = "image/right.png"
    div.append(image)

    var btn = document.getElementById("myBtn");

    var span = document.getElementsByClassName("close")[0];

    var para = document.createElement("p")
    var x = document.createElement("strong")
    x.append("Success!")

    para.append(x)
    para.append("You have won the game.")
    div.append(para)


    modal.style.display = "block";

    span.onclick = function() {
    modal.style.display = "none";
    document.location.reload()
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            document.location.reload()
        }
    }
}