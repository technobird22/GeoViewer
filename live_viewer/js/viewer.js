function change_image(img){
    var image_site = "https://kiwiweather.com/";
    var image_directory = "gk-2a/";
    var path = image_site + image_directory + img;
    var tnpath = path.replace(img, img.replace(".", "-tn."));
    
    var display = document.getElementById("display")

    // alert("Changing Filter...\nFilter Requested: " + img + "\nChanging image display source to:\n" + path);
    
    display.src = path;
    display.scrollIntoView();

    // Will check for plurals
    var last_update = "[P] minute[s] ago"
                 // = "just now" // If updated this minute

    var next_update = "will be out in [P] minute[s]"
                 // = "<strong>is already available.</strong><br>
                 //    <button onclick="refresh_image()>Refresh Image</button>"

    document.getElementById("description").innerHTML = 
    "<h3>About:</h3> <br>" + about_img(img) + 
    "<br><i>This image was last updated " + last_update + ". The next image " + next_update + "</i>" +
    "<h3>Export:</h3>" +
    "Opens image in new tab: <br><button onclick=\"window.open('" + path + "', '_blank');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + tnpath + "', '_blank');\">" + "Reduced Quality" + "</button>" + 
    "<hr><h3>Statistics: </h3>" + 
    "Image update time: <span class=\"param\">" + " [PLACEHOLDER] " + "</span>" + 
    "<br>Image name: <span class=\"param\">" + img + "</span>";
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