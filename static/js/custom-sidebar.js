function updateMap(id){
	var toggle,location;
	switch(id){
	case 1:
		location = "#school";
		toggle = "#school-toggle";
		toggleSchool();
		break;
	case 2:
		location = "#clinic";
		toggle = "#clinic-toggle";
		toggleClinic();
		break;
	case 3:
		location = "#park";
		toggle = "#park-toggle";
		toggleParks();
		break;
	}
	$(location).toggleClass("active");
	$(toggle).toggleClass("hidden");
	
}
