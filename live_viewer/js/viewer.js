function change_image(img){
    var image_site = "https://kiwiweather.com/";
    var image_directory = "gk-2a/";
    var path = image_site + image_directory + img;
    var fullpath = path + ".jpg";
    var tnpath = path + "-tn.jpg";

    // alert("Changing Filter...\nFilter Requested: " + img + "\nChanging image display source to:\n" + path);
    document.getElementById("display").src = fullpath;
    document.getElementById("description").innerHTML = 
    "Image capture time: <br><span class=\"param\">" + " [PLACEHOLDER] " + "</span>" + 
    "<hr>About this image: <br><span class=\"param\">" + about_img(img) + "</span>" + 
    "<hr>Path to image: <br><span class=\"param\">" + fullpath + "</span>" + 
    "<hr>Open image in new tab: <br><button onclick=\"window.open('" + fullpath + "', '_blank');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + tnpath + "', '_blank');\">" + "Reduced Quality" + "</button>";
}

function about_img(img){
    // alert(img)
    switch(img){
        // Full disk images
        case "FD":
            return "This is the raw, unprocessed infra-red frame, as downloaded from the satellite.";
        case "clahe":
            return "This is the infra-red frame enhanced with CLAHE processing";
        case "sanchez":
            return "This is the colourized version of the raw infra-red image";

        // Charts and Predictions
        case "GWW3F":
            return "Global Wave Model data";
        case "UP50A":
            return "Pressure and temperature data for South-East Asia";
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