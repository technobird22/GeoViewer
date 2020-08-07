function change_enhancement(filter){
    var pass = "2020-06-01-21-35-48-NOAA_18";
    var image_directory = "images/page_for_all/";
    
    var path = image_directory + pass + "-" + filter + ".jpg";
    var tnpath = image_directory + pass + "-" + filter + "-tn.jpg";
    // var path = "images/page_for_all/".concat(pass, "-", filter, ".jpg");
    // alert("Changing Filter...\nFilter Requested: " + filter + "\nChanging image display source to:\n" + path);
    document.getElementById("display").src = path;
    document.getElementById("description").innerHTML = 
    "Pass ID: <br><span class=\"param\">" + pass + "</span>" + 
    "<hr>About this filter: <br><span class=\"param\">" + about_filter(filter) + "</span>" + 
    "<hr>Path to filter image: <br><span class=\"param\">" + location.href.replace("/passes.html", "") + "/" + path + "</span>" + 
    "<hr>Open filter image in new tab: <br><button onclick=\"window.open('" + location.href.replace("/passes.html", "") + "/" + path + "\', \'_blank\');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + location.href.replace("/passes.html", "") + "/" + tnpath + "\', \'_blank\');\">" + "Reduced Quality" + "</button>";
    // document.getElementById("description").innerHTML = path;
}

function about_filter(filter){
    switch(filter){
        case "za":
            return "Enhanced infra red image";
        case "no":
            return "No colour infrared enhanced image";
        case "mcir-precip":
            return "Coloured infrared image highlighting precipitation";
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
            return "Filter not found. Please submit an issue on GitHub for Albert (technobird22)";
    }
}