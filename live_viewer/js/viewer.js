function initialize_scripts(){
    set_data_site('https://kiwiweather.com/');
    // set_data_site(''); // For local viewing or tests
    magnify("display", 3);
}

// Global variables
var data_site;

var img;
var path;
var tnpath;

var show_full_preview = false;
var is_magnifier_on = false;
var is_instructions = true;

// Set site from which data is retreived
function set_data_site(img_site){
    data_site = img_site;
}

// (For testing): Show alert with current path
function whatpath(){
    alert("Path is: " + path);
}

// Change video source
function change_video(new_img){
    img = new_img
    var data_directory = "gk-2a/";
    path = data_site + data_directory + img;
    
    var display = document.getElementById("display")
    var vid_display = document.getElementById("video_display")
    
    vid_display.src = path;

    display.style.display = "none";
    vid_display.style.display = "initial";
    disable_magnifier()

    // Will check for plurals
    var last_update = "[P] minute[s] ago"
    // = "just now" // If updated this minute
    
    var next_update = "will be out in [P] minute[s]"
    // = "<strong>is already available.</strong><br>
    //    <button onclick="refresh_image()>Refresh Image</button>"
    
    vid_display.scrollIntoView();

    // Update page info
    document.getElementById("description").innerHTML = 
    "<h3 class='small-header'>About:</h3> <br>" + about_data() + 
    "<br><i>This video was last updated " + last_update + ". The next video " + next_update + "</i>" +
    "<h3 class='small-header'>Export:</h3>" +
    "Open video in new tab: <br><button onclick=\"window.open('" + path + "', '_blank');\">" + "Original Quality" + "</button>" +
    "<hr><h3>Statistics: </h3>" + 
    "Video update time: <span class=\"param\">" + " [PLACEHOLDER] " + "</span>" + 
    "<br>Video name: <span class=\"param\">" + img + "</span>";

    setTimeout(function(){
        vid_display.play();
    }, 500);
}

// Refresh the whole page
function refresh_page(){
    location.reload();
}

// Change image source
function change_image(new_img){
    img = new_img
    
    var data_directory = "gk-2a/";
    path = data_site + data_directory + img;
    tnpath = path.replace(img, img.replace(".", "-tn."));
    
    var display = document.getElementById("display")
    var vid_display = document.getElementById("video_display")

    display.style.display = "initial";
    vid_display.style.display = "none";

    refresh_image();
}

// Refresh image source
function refresh_image(){
    var display = document.getElementById("display")

    // alert("Refreshing data...");
    if(is_instructions){
        is_magnifier_on = true;
        is_instructions = false;
    }
    
    if(show_full_preview){
        display.src = path;
    } else{
        display.src = tnpath;
    }

    var magnifier = document.getElementById("magnifier");
    magnifier.style.backgroundImage = "url('" + path + "')";

    // Will check for plurals
    var last_update = "[P] minute[s] ago"
    // = "just now" // If updated this minute
    
    var next_update = "will be out in [P] minute[s]"
    // = "<strong>is already available.</strong><br>
    //    <button onclick="refresh_image()>Refresh Image</button>"
    
    display.scrollIntoView();

    // Update page info
    document.getElementById("description").innerHTML = 
    "<h3 class='small-header'>About:</h3> <br>" + about_data() + 
    "<br><i>This image was last updated " + last_update + ". The next image " + next_update + "</i>" +
    "<h3 class='small-header'>Export:</h3>" +
    "Open image in new tab: <br><button onclick=\"window.open('" + path + "', '_blank');\">" + "Original Quality" + "</button>" +
    "<button onclick=\"window.open('" + tnpath + "', '_blank');\">" + "Reduced Quality" + "</button>" + 
    
    // "Download image: <br><a href='" + path + "' download><button>" + "Original Quality" + "</button></a>" +
    // " <br><a href='" + tnpath + "' download><button>" + "Reduced Quality" + "</button></a>" + 
    "<hr><h3>Statistics: </h3>" + 
    "Image update time: <span class=\"param\">" + " [PLACEHOLDER] " + "</span>" + 
    "<br>Image name: <span class=\"param\">" + img + "</span>";

    update_magnifier_dimensions();
}

// Return information about a specific image
function about_data(){
    switch(img){
        // Full disk images
        case "FD.jpg":
            return "This is the raw, unprocessed infra-red frame, as downloaded from the satellite.";
        case "clahe.jpg":
            return "This is the infra-red frame enhanced with CLAHE processing";
        case "sanchez.jpg":
            return "This is the colourized version of the raw infra-red image";

        // Animations
        case "FD-_sanchez-143.mp4":
            return "This is an animation of the image data from the last 24 hours, colourised using Sanchez, by NullPainter";
        case "FD-_sanchez-715.mp4":
            return "This is an animation of the image data from the last 72 hours, colourised using Sanchez, by NullPainter";
        case "FD-raw-143.mp4":
            return "This is an animation of the image data from the last 24 hours, received as-is from the satellite, with no processing";
        case "FD-raw-715.mp4":
            return "This is an animation of the image data from the last 72 hours, received as-is from the satellite, with no processing";

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
        
        // Other data
        case "wxfox.png":
        return "Weather fox image for testing";
        
        default:
            return "Requested image not found. Please submit an issue on GitHub for Albert (technobird22)";
    }
}

// Expand image display
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

// Show options / minimize image
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
    selection.style.width = "28%";

    display.style.width = "70%";
}

function disable_magnifier(){
    document.getElementById("magnifier_on").checked = false;
    magnifier_option();
}

// Magnifier scripts
var w, h, bw, zoom;
function magnifier_option(){
    var checkBox = document.getElementById("magnifier_on");
    var mag_instructions = document.getElementById("magnifier_instructions");

    if (checkBox.checked == true){
        is_magnifier_on = true;

        mag_instructions.innerHTML = "Hover over image to magnify";
    } else{
        if(is_instructions){
            is_instructions = false;
        }
        is_magnifier_on = false;

        mag_instructions.innerHTML = "Magnifier is disabled";

        glass = document.getElementById("magnifier");
        glass.style.visibility = "hidden";

        // If the magnifier is disabled, show the full quality image
        document.getElementById("full_size_prev").checked = true;
        full_size_option();
    }
}

// Option to make preview image full size
function full_size_option(){
    var checkBox = document.getElementById("full_size_prev");

    if (checkBox.checked == true){
        show_full_preview = true;
    } else{
        show_full_preview = false;
    }
}

// Fox
function fox(){
    set_data_site('');
    show_full_preview = true;

    change_image('wxfox.png')

    show_full_preview = false;
    initialize_scripts()
}

// Update dimentions of magnifier when image is changed
function update_magnifier_dimensions(){
    var glass = document.getElementById("magnifier")
    var data = document.getElementById("display")

    bw = 3;
    w = glass.offsetWidth / 2;
    h = glass.offsetHeight / 2;

    glass.style.backgroundSize = (data.width * zoom) + "px " + (data.height * zoom) + "px";
}

// Magnify the display on mouseover
// Credit: https://www.w3schools.com/howto/howto_js_image_magnifier_glass.asp
function magnify(imgID, curzoom){
    zoom = curzoom;

    var data, glass;
    data = document.getElementById(imgID);
  
    /* Create magnifier glass: */
    glass = document.createElement("DIV");
    glass.setAttribute("id", "magnifier");
    
    /* Insert magnifier glass: */
    data.parentElement.insertBefore(glass, data);
    
    /* Set background properties for the magnifier glass: */
    glass.style.visibility = "hidden";
    glass.style.backgroundRepeat = "no-repeat";
    glass.style.backgroundSize = (data.width * zoom) + "px " + (data.height * zoom) + "px";

    /* Execute a function when someone moves the magnifier glass over the image: */
    glass.addEventListener("mousemove", move_magnifier);
    data.addEventListener("mousemove", move_magnifier);
  
    /*and also for touch screens:*/
    glass.addEventListener("touchmove", move_magnifier);
    data.addEventListener("touchmove", move_magnifier);

    // $("#display").mouseover(function(){
    //     $("#magnifier").css("visibility", "visible");
    // });

    function move_magnifier(e) {
        update_magnifier_dimensions();

        var pos, x, y;
        /* Prevent any other actions that may occur when moving over the image */
        // e.preventDefault();

        /* Get the cursor's x and y positions: */
        pos = get_cursor_pos(e);
        x = pos.x;
        y = pos.y;


        /* Prevent the magnifier glass from being positioned outside the image: */
        /* Hide magnifier if it is about to be */
        if(x > data.width - (w / zoom)){
            x = data.width - (w / zoom);
            glass.style.visibility = "hidden";
        } else if(x < w / zoom){
            x = w / zoom;
            glass.style.visibility = "hidden";
        } else if(y > data.height - (h / zoom)){
            y = data.height - (h / zoom);
            glass.style.visibility = "hidden";
        } else if(y < h / zoom){
            y = h / zoom;
            glass.style.visibility = "hidden";
        } else if(is_magnifier_on){
            glass.style.visibility = "visible";
        }
        
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
        a = data.getBoundingClientRect();
        /* Calculate the cursor's x and y coordinates, relative to the image: */
        x = e.pageX - a.left;
        y = e.pageY - a.top;
        /* Consider any page scrolling: */
        x = x - window.pageXOffset;
        y = y - window.pageYOffset;
        return {x : x, y : y};
    }
}
