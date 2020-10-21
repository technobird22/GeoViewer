function initialize_scripts(){
    // document.getElementById("options_button").style.display = "none";
    magnify("display", 3);
}

function change_image(image_site, img){
    // var image_site = "https://kiwiweather.com/";
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

    var magnifier = document.getElementById("magnifier");
    magnifier.style.backgroundImage = "url('" + path + "')";
    magnifier.style.visibility = "";

    update_magnifier_dimensions();
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
        
        case "wxfox.png":
        return "Weather fox image for testing";
        
        default:
            return "Requested image not found. Please submit an issue on GitHub for Albert (technobird22)";
    }
}

function expand_img(){
    var selection = document.getElementById("filter-select");
    var display = document.getElementById("image-display");
    var enhancements_list = document.getElementById("enhancements");
    
    document.getElementById("image_types_heading").style.display = "none";

    document.getElementById("full_screen_button").style.display = "none";
    document.getElementById("options_button").style.display = "initial";
    
    selection.style.height = "50px";
    selection.style.width = "100%";

    display.style.width = "100%";

    setTimeout(function(){
        selection.style.overflow = "hidden";
        // enhancements_list.style.display = "none";
        selection.style.backgroundColor = "lightblue";
    }, 750);
}

function show_options(){
    var selection = document.getElementById("filter-select");
    var display = document.getElementById("image-display");
    var enhancements_list = document.getElementById("enhancements");
    
    selection.style.overflow = "visible";
    // enhancements_list.style.display = "initial";
    selection.style.backgroundColor = "white";

    document.getElementById("image_types_heading").style.display = "initial";

    document.getElementById("full_screen_button").style.display = "initial";
    document.getElementById("options_button").style.display = "none";
    
    selection.style.height = "1300px";
    selection.style.width = "30%";

    display.style.width = "70%";
}

var w, h, bw, zoom;
function update_magnifier_dimensions(){
    var glass = document.getElementById("magnifier")
    var img = document.getElementById("display")

    bw = 3;
    w = glass.offsetWidth / 2;
    h = glass.offsetHeight / 2;

    glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";
}

// Magnify the display on mouseover
// Credit: https://www.w3schools.com/howto/howto_js_image_magnifier_glass.asp
function magnify(imgID, curzoom){
    zoom = curzoom;

    var img, glass;
    img = document.getElementById(imgID);
  
    /* Create magnifier glass: */
    glass = document.createElement("DIV");
    glass.setAttribute("id", "magnifier");
    
    /* Insert magnifier glass: */
    img.parentElement.insertBefore(glass, img);
    
    /* Set background properties for the magnifier glass: */
    glass.style.visibility = "hidden";
    glass.style.backgroundRepeat = "no-repeat";
    glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";

    /* Execute a function when someone moves the magnifier glass over the image: */
    glass.addEventListener("mousemove", move_magnifier);
    img.addEventListener("mousemove", move_magnifier);
  
    /*and also for touch screens:*/
    glass.addEventListener("touchmove", move_magnifier);
    img.addEventListener("touchmove", move_magnifier);

    // $("#display").mouseover(function(){
    //     $("#magnifier").css("visibility", "visible");
    // });

    function move_magnifier(e) {
        update_magnifier_dimensions();

        var pos, x, y;
        /* Prevent any other actions that may occur when moving over the image */
        e.preventDefault();

        /* Get the cursor's x and y positions: */
        pos = get_cursor_pos(e);
        x = pos.x;
        y = pos.y;
        

        /* Prevent the magnifier glass from being positioned outside the image: */
        if (x > img.width - (w / zoom)) {x = img.width - (w / zoom);}
        if (x < w / zoom) {x = w / zoom;}
        if (y > img.height - (h / zoom)) {y = img.height - (h / zoom);}
        if (y < h / zoom) {y = h / zoom;}
        /* Set the position of the magnifier glass: */
        glass.style.left = (x - w) + "px";
        glass.style.top = (y - h) + "px";
        /* Display what the magnifier glass "sees": */
        glass.style.backgroundPosition = "-" + ((x * zoom) - w + bw) + "px -" + ((y * zoom) - h + bw) + "px";
    }
  
    function get_cursor_pos(e) {
        var a, x = 0, y = 0;
        e = e || window.event;
        /* Get the x and y positions of the image: */
        a = img.getBoundingClientRect();
        /* Calculate the cursor's x and y coordinates, relative to the image: */
        x = e.pageX - a.left;
        y = e.pageY - a.top;
        /* Consider any page scrolling: */
        x = x - window.pageXOffset;
        y = y - window.pageYOffset;
        return {x : x, y : y};
    }
}