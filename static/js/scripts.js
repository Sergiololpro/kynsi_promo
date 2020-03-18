$(document).ready(function() {

    // Слайдер на главной
    if ($('.block_3__slider').length) {
        $('.block_3__slider').slick({
            slidesToShow: 2,
            slidesToScroll: 2,
            arrows: false,
            autoplay: true,
            responsive: [
                {
                  breakpoint: 1025,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                }
            ]
        });
    }

    // Слайдер брендов
    if ($('.block_6__slider').length) {
        $('.block_6__slider').slick({
            slidesToShow: 7,
            slidesToScroll: 7,
            prevArrow: '<div class="block_6__nav block_6__nav-prev"></div>',
            nextArrow: '<div class="block_6__nav block_6__nav-next"></div>',
            responsive: [
                {
                  breakpoint: 1400,
                  settings: {
                    slidesToShow: 5,
                    slidesToScroll: 5
                  }
                },
                {
                  breakpoint: 1025,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3
                  }
                },
                {
                  breakpoint: 640,
                  settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                  }
                }
            ]
        });
    }

    // Слайдер у салонов
    // if ($('.block_8__img').length) {
    //     $('.block_8__img').slick({
    //         slidesToShow: 1,
    //         slidesToScroll: 1,
    //         arrows: false,
    //         autoplay: true,
    //         fade: true
    //     });
    // }

    // Слайдер у салонов вверхну
    if ($('.salons_slider').length) {
        $('.salons_slider').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
            autoplay: true,
            fade: true,
            autoplaySpeed: 1000,
            dots: true
        });
    }

    // Слайдер instagram
    // if ($('.block_9__slider').length) {
    //     $('.block_9__slider').slick({
    //         slidesToShow: 1,
    //         slidesToScroll: 1,
    //         arrows: false,
    //         autoplay: true,
    //         fade: true
    //     });
    // }
    
    // Телефоны в шапке
    $(".header__phone").on("click", function () {
        $(this).toggleClass('active');
    });

    // Скролл
    $(window).on('scroll load', function () {

        // Телефоны
        if ($('.header__phone').length) {
            $('.header__phone').removeClass('active');
        }
    
        animations();
    });

    // Навигация
    $(".header__nav").on("click", function() {
        var id = $(this).data('nav');
            $('.header__navs, .header__menu').removeClass('active');

        if (id) {
            $('body, html').animate({
                scrollTop: $("#" + id).offset().top - 100
            }, 800);
        }
    });

    // Услуги
    // $(".block_5__name").on("click", function () {
    //     $('.block_5__name, .block_5__wrp').removeClass('active');

    //     $(this).addClass('active');
    //     $('.block_5__wrp:nth-child(' + parseInt($(this).index() + 1) + ")").addClass('active');
    // });

    // Видео на баннере
    // $("#banner__video").YTPlayer({
    //     mute: true,
    //     showControls: false,
    //     containment: '#banner__video',
    //     loop: true,
    //     autoPlay: true
    // });

    // $("#banner__video").YTPPlay();

    // $("#banner__video").trigger("click");

    // Меню
    $(".header__menu").on("click", function () {
        $(this).toggleClass('active');
        $('.header__navs').toggleClass('active');
    });

    // Вверх
    $(".header__logo:not(a)").on("click", function() {
        $('body, html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

    // Цель
    $(".widget").on("click", function() {
        // jivo_api.open();
        yaCounter18944653.reachGoal('online_registration');
    });

    // Цель whatsapp
    $(".header__nav-whatsapp").on("click", function() {
        yaCounter18944653.reachGoal('WhatsApp');
    });

    // Подмена контента
    if ((window.location.href.indexOf("utm_source") !== -1)) {
        // Слайдер баннер
        if ($('.banner__wrapper').length) {
            $('.banner__wrapper').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                autoplay: true,
                fade: true,
                autoplaySpeed: 3000,
                dots: true
            });
        }

        $(".banner__wr-2, .block_7").addClass("active");
    } else {
        $(".banner__wr-2").remove();
    }

    // Открыть моадльник скидки
    $(".show_modal").on("click", function() {
        $(".overlay, .modal_discount").addClass("active");
        $("body").addClass("showed");
    });

    // Закрыть моадльник скидки
    $(".overlay, .modal__close").on("click", function() {
        $(".overlay, .modal").removeClass("active");
    });

    // Отправка почты в книгу
    $(".modal__button").on("click", function() {
        var id = "test",
            email,
            name;

        if ($("#disc_email").val().length) {
            email = $("#disc_email").val();
            name = $("#disc_email").val();
            
            if (window.location.href.toLowerCase().indexOf("utm_source=email&utm_medium=banner&utm_campaign=tickets") !== -1) {
                id = "88995918";
            } else if (window.location.href.toLowerCase().indexOf("yandex_maps") !== -1) {
                id = "2303208";
            } else if (window.location.href.toLowerCase().indexOf("google_maps") !== -1) {
                id = "2305777";
            } else if (window.location.href.toLowerCase().indexOf("fb") !== -1) {
                id = "2179834";
            } else if (window.location.href.toLowerCase().indexOf("instagram") !== -1) {
                id = "2179835";
            } else if (window.location.href.toLowerCase().indexOf("yandex") !== -1) {
                id = "2179832";
            } else if (window.location.href.toLowerCase().indexOf("google") !== -1) {
                id = "2179884";
            } else if (window.location.href.toLowerCase().indexOf("ig") !== -1) {
                id = "88944312";
            }
            
            $.ajax({
                url: '/ajax/',
                method: "POST",
                data: {id: id, email: email, name: name},
                success: function (data, textStatus){
                    $(".modal_discount .modal__content-main").removeClass("active");
                    $(".modal_discount .modal__content-success").addClass("active");

                    // Цель
                    yaCounter18944653.reachGoal('discount');
                }
            })
        }
    });

    // Открыть услуги на моб.
    $(".block_1__title").on("click", function() {
        if ($(this).hasClass("block_1__title-hairs")) {
            $(".block_1__title-hairs").parent().find(".block_5__hide").toggleClass("active");
            $(".block_1__title-hairs").parent().toggleClass("active");
        } else if ($(this).hasClass("block_1__title-carry")) {
            $(".block_1__title-carry").parent().find(".block_5__hide").toggleClass("active");
            $(".block_1__title-carry").parent().toggleClass("active");
        } else {
            $(this).parent().find(".block_5__hide").toggleClass("active");
        }
    });

    // На салоны
    $(".to_salons").on("click", function() {
        $('body, html').animate({
            scrollTop: $("#salons").offset().top - 100
        }, 800);
    });

    // Цели на оналйн запись
    $(document).bind("reservi_order", function(){
        gtag('event', 'online', {'event_category': 'order'});
        yaCounter18944653.reachGoal('order-online');
    });

    // Анимации
    function animations() {
        $(".animation:not(.animated)").each(function () {
            var windowTop = $(window).height() * .9 + $(window).scrollTop(),
                objectTop = $(this).offset().top;

            if (windowTop > objectTop) {
                $(this).addClass('animated');
            }
        });
    }

    $(window).on('resize load', function () {
        // Видео на баннере
        if ($('.banner__video').length) {
            if (($('.banner__video').width() / $('.banner__video').height()) > 1.777){
                $('.banner__video').addClass('rotated');
            }

            $('.banner__video').addClass('active');
        }
    });

    // Lazyload
    //$(".lazyload").lazyload();

    // Открыть живосайт
    $(".jivo").on("click", function() {
        jivo_api.open();
    });

    // Слайдер сертификатов
    if ($('.certs_slider').length) {
        $('.certs_slider').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            prevArrow: '<div class="certs__nav certs__nav-prev"></div>',
            nextArrow: '<div class="certs__nav certs__nav-next"></div>',
            // autoplay: true,
            autoplaySpeed: 3000,
            dots: true,
            appendDots: $('.certs__radios'),
            customPaging: function(slick, index) {
                var text = $(slick.$slides[index]).data('text');
                return '<div class="certs__radio">' + text + '</div>';
            },
            responsive: [
                {
                  breakpoint: 640,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                }
            ]
        });
    }

    // Появление модальника со скидкой
    if (window.location.href.toLowerCase().indexOf("utm") !== -1) {
        setTimeout(function() {
            if (!$("body").hasClass("showed")) {
                $(".overlay, .modal_discount").addClass("active");
            }
        }, 15000);
    }

    // Сертификаты якорь
    $(".to_certs").on("click", function() {
        $('body, html').animate({
            scrollTop: $("#certs").offset().top - 100
        }, 800);
    });

    // Открыть моадльник скидки
    $(".show_cert").on("click", function() {
        $(".overlay, .modal_cert").addClass("active");
        $("body").addClass("showed");
    });

    // Открыть моадльник KYNSI BOX
    $(".show_box").on("click", function() {
        $(".overlay, .modal_box").addClass("active");
        $("body").addClass("showed");
    });

    // Отправка информации по сертификату
    $(".modal__button").on("click", function() {
        var name, phone, nominal, utm,
            $modal = $(this).closest(".modal");

        $modal.find("[name='phone']").removeClass("error");

        if ($modal.find("[name='phone']").val().length) {
            name = $modal.find("[name='name']").val();
            phone = $modal.find("[name='phone']").val();
            nominal = $modal.find("[name='nominal']").val();
            utm = window.location.href.split("?")[1];

            $.ajax({
                url: '/sendmail/',
                method: "POST",
                data: {name: name, phone: phone, nominal: nominal, utm: utm},
                success: function (data, textStatus){
                    $modal.find(".modal__content-main").removeClass("active");
                    $modal.find(".modal__content-success").addClass("active");

                    yaCounter18944653.reachGoal('sertificate');
                }
            });
        } else {
            $modal.find("[name='phone']").addClass("error");
        }
    });

    // Открыть информацию
    $(".certs_slider__info").on("click", function() {
        $(".overlay, .modal_info").addClass("active");
    });

});