  var swiper = new Swiper(".cat-slider", {
    slidesPerView: 2,
    spaceBetween: 20,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 5,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 7,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".doctor-slider", {
    slidesPerView: 1,
    spaceBetween: 20,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 5,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".bim-slider", {
    slidesPerView: 4,
    spaceBetween: 20,
    loop: true,
    speed: 5000,
    autoplay: {
      enabled: true,
      delay: 1,
      },
      breakpoints: {
        640: {
          slidesPerView: 5,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 7,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 12,
          spaceBetween: 15,
        },
      },
  });




  var swiper = new Swiper(".comment-slider", {
    slidesPerView: 1,
    spaceBetween: 20,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".blog-slider", {
    slidesPerView: 1,
    spaceBetween: 20,
    autoplay: {
        delay: 5000,
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 15,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 15,
        },
        1024: {
          slidesPerView: 4,
          spaceBetween: 15,
        },
      },
  });

  var swiper = new Swiper(".partners", {
    slidesPerView: 2,
    spaceBetween: 10,
    breakpoints: {
      640: {
        slidesPerView: 4,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 5,
        spaceBetween: 10,
      },
    },
    
  });



  var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    cursorChar: '',
    loop: true,
    backDelay: 1000,
    startDelay: 500,
    typeSpeed: 100,
  });

