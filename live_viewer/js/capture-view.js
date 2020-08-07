function change_image(img){
    var pass = "2020-06-01-21-35-48-NOAA_18";
    var image_directory = "images/page_for_all/";
    
    var path = image_directory + pass + "-" + img + ".jpg";
    var tnpath = image_directory + pass + "-" + img + "-tn.jpg";
    // var path = "images/page_for_all/".concat(pass, "-", img, ".jpg");
    // alert("Changing Filter...\nFilter Requested: " + img + "\nChanging image display source to:\n" + path);
    document.getElementById("display").src = path;
    document.getElementById("description").innerHTML = 
    "Image capture time: <br><span class=\"param\">" + pass + "</span>" + 
    "<hr>About this image: <br><span class=\"param\">" + about_img(img) + "</span>" + 
    "<hr>Path to image: <br><span class=\"param\">" + location.href.replace("/passes.html", "") + "/" + path + "</span>" + 
    "<hr>Open image in new tab: <br><button onclick=\"window.open('" + location.href.replace("/passes.html", "") + "/" + path + "\', \'_blank\');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + location.href.replace("/passes.html", "") + "/" + tnpath + "\', \'_blank\');\">" + "Reduced Quality" + "</button>";
    // document.getElementById("description").innerHTML = path;
}

function about_img(img){
    // alert(img)
    switch(img){
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
            return "Requested image not found. Please submit an issue on GitHub for Albert (technobird22)";
    }
}