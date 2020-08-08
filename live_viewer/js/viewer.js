function change_image(img){
    var image_site = "https://kiwiweather.com/";
    var image_directory = "gk-2a/";
    var path = image_site + image_directory + img;
    var tnpath = path.replace(img, img.replace(".", "-tn."));
    
    var display = document.getElementById("display")

    // alert("Changing Filter...\nFilter Requested: " + img + "\nChanging image display source to:\n" + path);
    
    display.src = path;
    display.scrollIntoView();

    document.getElementById("description").innerHTML = 
    "Image update time: <br><span class=\"param\">" + " [PLACEHOLDER] " + "</span>" + 
    "<hr>About this image: <br><span class=\"param\">" + about_img(img) + "</span>" + 
    "<hr>Path to image: <br><span class=\"param\">" + path + "</span>" + 
    "<hr>Open image in new tab: <br><button onclick=\"window.open('" + path + "', '_blank');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + tnpath + "', '_blank');\">" + "Reduced Quality" + "</button>";
}

function about_img(img){
    // alert(img)
    switch(img){
        // Full disk images
        case "FD.jpg":
            return "This is the raw, unprocessed infra-red frame, as downloaded from the satellite.";
        case "clahe.jpg":
            return "This is the infra-red frame enhanced with CLAHE processing";
        case "sanchez.jpg":
            return "This is the colourized version of the raw infra-red image";

        // Charts and Predictions
        case "GWW3F.gif":
            return "Global Wave Model data";
        case "UP50A.gif":
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