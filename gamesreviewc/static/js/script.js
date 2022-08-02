 document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // Drop Down initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
    
    collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
    
    //delete modal initialization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
});

//Due to using materialize Javascript frame work code this will throw up errors on JSlint 