function updateMap(id) {
    var toggle,
        location,
        checkBox;
    var update = true;
    switch (id) {
        case 1:
            location = "#school";
            toggle = "#school-toggle";
            checkBox = "#checkbox_school";
            break;
        case 2:
            location = "#clinic";
            toggle = "#clinic-toggle";
            checkBox = "#checkbox_clinic";
            break;
        case 3:
            location = "#park";
            toggle = "#park-toggle";
            checkBox = "#checkbox_park";
            break;
        case 4:
            update = false;
            location = "#radius";
            toggle = "#radius-toggle";
            break;
        case 5:
            location = "#gym";
            toggle = "#gym-toggle";
            checkBox = "#checkbox_gym";
            break;
        case 6:
            location = "#community";
            toggle = "#community-toggle";
            checkBox = "#checkbox_community";
            break;
    }
    $(location).toggleClass("active");
    $(toggle).toggleClass("hidden");
    if (update) {
        $(checkBox).prop("checked", !$(checkBox).prop("checked"));
    }
    switch (id) {
        case 1:
            toggleSchool();
            break;
        case 2:
            toggleClinic();
            break;
        case 3:
            toggleParks();
            break;
        case 4:
            if (!$(toggle).hasClass('hidden')) {
                $("#ex1").slider("enable");
                createRadius();
                toggleAll();
            } else {
                $("#ex1").slider("disable");
                removeCircles();
            }
            break;
        case 5:
            toggleGym();
            break;
        case 6:
            toggleCommunity();
            break;
    }
}
