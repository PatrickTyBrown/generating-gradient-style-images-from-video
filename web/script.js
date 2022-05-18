function size_button_clicked(){
    console.log('click')
    if (document.getElementById("custom_size").checked){
        document.getElementById("x_size").disabled = false;
        document.getElementById("y_size").disabled = false;
    }
    else {
        document.getElementById("x_size").disabled = true;
        document.getElementById("y_size").disabled = true;
    }
}

function file_selection_changed(){
    if (document.getElementById("file_input").value){
        document.getElementById("submit_button").disabled = false;
    }
    else {
        document.getElementById("submit_button").disabled = true;
    }
}

function cancel_button_clicked(){
    location.reload()
}

function get_active_size(){
    if (document.getElementById("custom_size").checked){
        return 'custom'
    }
    if (document.getElementById("default_size").checked){
        return 'default'
    }
    if (document.getElementById("source_size").checked){
        return 'source'
    }
    else{
        return 'default'
    }
}

// filename, coloring = 'single', method = 'mean', increment='default', added_thickness=0, size = 'default', x_size = 0, y_size = 0
function submit_button_clicked(){
    var file = document.getElementById("file_input").files[0].name;
    var color = document.getElementById("style_input").value;
    var method_ = document.getElementById("method_input").value;
    var incr = 'default'//document.getElementById("style_input").value;
    var added = 0//document.getElementById("style_input").value;
    var sizing = get_active_size()
    var x = document.getElementById("x_size").value;
    var y = document.getElementById("y_size").value;
    eel.run_image_generation(filename = file, coloring = color, method=method_, increment=incr, added_thickness=added, size=sizing, x_size=x, y_size=y)
}

document.getElementById("custom_size").addEventListener("click", size_button_clicked)
document.getElementById("default_size").addEventListener("click", size_button_clicked)
document.getElementById("source_size").addEventListener("click", size_button_clicked)
document.getElementById("file_input").addEventListener("change", file_selection_changed)
document.getElementById("cancel_button").addEventListener("click", cancel_button_clicked)
document.getElementById("submit_button").addEventListener("click", submit_button_clicked)