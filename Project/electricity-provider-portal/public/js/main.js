(function($){
    "use strict";
    // Convert All Image to SVG
    $('img.svg').each(function() {
         var $img = $(this),
             imgID = $img.attr('id'),
             imgClass = $img.attr('class'),
             imgURL = $img.attr('src');

         $.get(imgURL, function(data) {
             // Get the SVG tag, ignore the rest
             var $svg = $(data).find('svg');

             // Add replaced image's ID to the new SVG
             if (typeof imgID !== 'undefined') {
                 $svg = $svg.attr('id', imgID);
             }
             // Add replaced image's classes to the new SVG
             if (typeof imgClass !== 'undefined') {
                 $svg = $svg.attr('class', imgClass);
             }

             // Remove any invalid XML tags as per http://validator.w3.org
             $svg = $svg.removeAttr('xmlns:a');

             // Replace image with new SVG
             $img.replaceWith($svg);
        }, 'xml');
    });

    //back to top
    var backtotop = $(".backtotop");
        backtotop.on('click', function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1500);
    });

    // Headroom
    var myElement = document.querySelector(".headroom");
    var headroom  = new Headroom(myElement);
    headroom.init(); 

    $(window).on('scroll',function(){
        if ($(this).scrollTop() > 150) {
            $('header').addClass("hide-topbar");
        } else {
            $('header').removeClass("hide-topbar");
        }

        /* Back to top */
        if ($(this).scrollTop() > 400) {
            backtotop.fadeIn(500);
        } else {
            backtotop.fadeOut(500);
        }
    });

    //for mobile menu
    $( '.toggle-inner' ).on( 'click', function (e) {
        e.preventDefault();
        var mask = '<div class="mask-overlay">';

        $( 'body' ).toggleClass( 'active' );
        $(mask).hide().appendTo( 'body' ).fadeIn( 'fast' );
        $( '.mask-overlay, .close-menu' ).on( 'click', function() {
            $( 'body' ).removeClass( 'active' );
            $( '.mask-overlay' ).remove();
        });
    });
    
    var Accordion = function (el, multiple) {
        this.el = el || {};

        this.multiple = multiple || false;

        var dropdownlink = this.el.find('.dropdownlink');
        dropdownlink.on('click', {
                el: this.el,
                multiple: this.multiple
            },
            this.dropdown);
    };
    
    Accordion.prototype.dropdown = function (e) {
        e.preventDefault();
        var $el = e.data.el,
             $this = $(this),

            $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            //show only one menu at the same time
            $el.find('.submenuItems').not($next).slideUp().parent().removeClass('open');
        }
    }
    var accordion = new Accordion($('.accordion-menu'), false);

    //swipper runner
    $('.swiper-container').each(function() {
        new SwiperRunner($(this));
    });
    
    // Section Background Image
    $('[data-bg-image]').each(function() {
        var img = $(this).data('bg-image');
        $(this).css({
         backgroundImage: 'url(' + img + ')',
        });
    });
    
    //counterup
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
    
    //hover tab
    $('#whc_myHover_Tab').on('mouseenter.bs.tab.data-api', '[data-toggle="tab"], [data-hover="tab"]', function () {
      $(this).tab('show');
    });
    
    //range slider  
    $('input[type="range"]').rangeslider({
        polyfill: false,
        onSlide:function(position, value){
          var $class = '.item' + value;

          $('.whc_range_plan .whc_range_item').removeClass('active');
          $($class, '.whc_range_plan').addClass('active');
        }
    });
    
    //progress bar
    var waypoints = $('.progress-bar').waypoint(function(direction) {
        $('.progress .progress-bar').progressbar();
    }, {
        offset: '10%'
    });

    //marquee
    $('.marquee').marquee({
        duration: 25000,
        gap: 30,
        duplicated: true,
        pauseOnHover: true,
        startVisible: true
    });
    
    //blog masonry
    var $postmasonry = $('.all_post');
    $postmasonry.masonry({
        itemSelector: '.post_item',
        columnWidth: '.post-sizer',
        percentPosition: true
    });

    $(window).on('resize',function() {
        $postmasonry.masonry('bindResize')
    });


    //preloader
    $(window).load(function() {
        $(".preloader").delay(3000).fadeOut("slow");
    });
    
    //Parallax Background
    $(window).on('scroll',function(){
        $('[data-parallax="image"]').each(function() {
            var actualHeight = $(this).position().top;
            var speed      = $(this).data('parallax-speed');
            var reSize     = actualHeight - $(window).scrollTop();
            var makeParallax = -(reSize/2);
            var posValue   = makeParallax + "px";

            $(this).css({
                backgroundPosition: '50% ' + posValue,
            });
        });
    });
    
    //google map
    $('.map').each(function() {
        var $this  = $(this);

        $this.gmap3({
            center:[37.2755928,-104.6569351],
            zoom:2,
            mapTypeId: "shadeOfGrey",
            mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, "shadeOfGrey"]
            }
        })
      .styledmaptype(
        "shadeOfGrey",
        [
            {
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "landscape",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "hue": "#e9e9e9"
                    },
                    {
                        "saturation": -100
                    },
                    {
                        "lightness": 100
                    }
                ]
            },
            {
                "featureType": "water",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "hue": "#e9e9e9"
                    },
                    {
                        "lightness": 50
                    },
                    {
                        "saturation": -100
                    }
                ]
            },
            {
                "featureType": "administrative.province",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "administrative.country",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "labels",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "road.local",
                "elementType": "geometry.fill",
                "stylers": [
                    {
                        "visibility": "off"
                    },
                    {
                        "color": "#e9e9e9"
                    },
                    {
                        "lightness": 90
                    }
                ]
            }
        ],
        {
            name: "Shades of Grey"
        })
        .marker([
            {position:[37.2755928,-104.6569351],icon: "images/map-marker-on.png"},
            {address:"Munich, Germany", icon: "images/map-marker-off.png"},
            {address:"Indiana, USA", icon: "images/map-marker-off.png"},
            {address:"California, USA", icon: "images/map-marker-off.png"},
            {address:"Airport Blvd, Singapore", icon: "images/map-marker-off.png"},
            {address:"Toronto, Canada", icon: "images/map-marker-off.png"},
            {icon: "images/map-marker-off.png", icon: "images/map-marker-off.png"}
        ])
        .on('click', function (marker) {
            marker.setIcon('images/map-marker-on.png');
        })
    });     

    //login
    document.querySelector('.whc_login_form').addEventListener('submit', function(event) {
        event.preventDefault();
      
        var email = document.getElementById('exampleInputEmail-login').value;
        var password = document.getElementById('exampleInputPassword-login-pass-2').value;
      
        fetch('http://localhost:8000/auth/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: email,
            password: password,
          }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
          console.error('Error:', error);
        });
      });

    //register
    document.querySelector('.whc_login_form').addEventListener('submit', function(event) {
        event.preventDefault();
      
        var firstName = document.querySelector('input[placeholder="First Name"]').value;
        var lastName = document.querySelector('input[placeholder="Last Name"]').value;
        var email = document.querySelector('input[placeholder="Enter you email ..."]').value;
        var password = document.querySelector('input[placeholder="*** *** ***"]').value;
      
        fetch('http://localhost:8000/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            email: email,
            password: password,
          }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
          console.error('Error:', error);
        });
      });
    
})(jQuery);