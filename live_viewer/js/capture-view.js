function change_image(img){
    var image_directory = "gk-2a/";
    var path = image_directory + img + ".jpg";
    var fullpath = location.href.replace("/captures.html", "") + "/" + path;
    var tnpath = image_directory + "-" + img + "-tn.jpg";
    // alert("Changing Filter...\nFilter Requested: " + img + "\nChanging image display source to:\n" + path);
    document.getElementById("display").src = path;
    document.getElementById("description").innerHTML = 
    "Image capture time: <br><span class=\"param\">" + " [PLACEHOLDER] " + "</span>" + 
    "<hr>About this image: <br><span class=\"param\">" + about_img(img) + "</span>" + 
    "<hr>Path to image: <br><span class=\"param\">" + fullpath + "</span>" + 
    "<hr>Open image in new tab: <br><button onclick=\"window.open('" + fullpath + "', '_blank');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + location.href.replace("/passes.html", "") + "/" + tnpath + "', '_blank');\">" + "Reduced Quality" + "</button>";
    // document.getElementById("description").innerHTML = path;
}

function about_img(img){
    // alert(img)
    switch(img){
        case "FD":
            return "Raw unprocessed frame from the satellite";
        case "clahe":
            return "CLAHE enhanced image";
        case "sanchez":
            return "Colourized image";
        case "mcir":
            return "Coloured infrared image";
        case "therm":
            return "Air temperature image";
        case "sea":
            return "Sea surface temperature image";
        case "contrasta":
            return "Contrast - Channel A image";
        case "contrastb":
            return "Contrast - Channel B image";
        
        default:
            return "Requested image not found. Please submit an issue on GitHub for Albert (technobird22)";
    }
}