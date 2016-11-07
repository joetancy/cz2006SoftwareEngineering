function doIntro(){
	//alert("start!");
	doTour();
}
function doTour(){
  var tour = new Tour({
  steps: [
    {
      element: "#step1",
      title: "Search Housing",
      content: "Keep in an address and click search for HDB on sales on a particular location.",
      placement: "bottom",
      container: "body",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if (!$("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
    },
    {
      element: "#school",
      title: "School",
      content: "Click on the icon to toggle scools on the map. If radius is <strong>enabled</strong>, school will show within radius of the results",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    }, {
      element: "#clinic",
      title: "Clinic",
      content: "Click on the icon to toggle clinics on the map. If radius is <strong>enabled</strong>, clinics will show within radius of the results",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#park",
      title: "Park",
      content: "Click on the icon to toggle parks on the map. If radius is <strong>enabled</strong>, parks will show within radius of the results",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#gym",
      title: "Gym",
      content: "Click on the icon to toggle gyms on the map. If radius is <strong>enabled</strong>, gyms will show within radius of the results",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#community",
      title: "Community Club",
      content: "Click on the icon to toggle community club on the map. If radius is <strong>enabled</strong>, community club will show within radius of the results.",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#radius",
      title: "Radius",
      content: "Click on the icon to toggle radius on the map. If radius is <strong>enabled</strong>, all previously enabled toggles will be switch to show within the radius of HDB only.",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#radius-slider",
      title: "Radius Slider",
      content: "Radius slider is only enabled when radius icon is <strong>toggled</strong>, use this to control the radius surrounding the HDBs.",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#search",
      title: "Advance Search",
      content: "Perform reverse search based on the <strong>toggles</strong> selected. If radius is disabled, it will search with the default value of 500m.",
      container: "body",
      position: "right",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if ($("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".sidebar-nav");
        $(".tour-step-background").appendTo(".sidebar-nav");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#listing",
      title: "Listing",
      content: "View listing, Create listing or Remove your listing.",
      container: "body",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if (!$("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".navbar-collapse");
        $(".tour-step-background").appendTo("#listing");
        $(".tour-step-background").css("left", "0px");
      }
    },{
      element: "#account",
      title: "Account",
      content: "Register an account for more functionality of the website.",
      container: "body",
      backdrop: true,
      backdropContainer: 'body',
      onShow: function(){
        if (!$("#wrapper").hasClass('active')) {
          $("#wrapper").toggleClass("active");
        }
      },
      onShown: function() {
        $(".tour-backdrop").appendTo(".navbar-collapse");
        $(".tour-step-background").appendTo("#account");
        $(".tour-step-background").css("left", "0px");
      }
    }

  ]
});
  tour.init();
  tour.start(true).goTo(0);
}