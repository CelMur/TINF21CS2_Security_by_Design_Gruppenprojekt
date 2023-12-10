import React, { useState, useEffect } from 'react';

function App() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setIsLoading(false);
    }, 3000);
  }, []);

  if (isLoading) {
    return (
      <div>
        <div className="preloader">
          <div className="cloud cloud1"></div>
          <div className="cloud cloud2"></div>
          <div className="cloud cloud3"></div>
          <div className="cloud cloud4"></div>
          <div className="cloud cloud5"></div>
          <div className="cloud cloud6"></div>
          <div className="sun-circle">
            <h1>SBD</h1>
          </div>
        </div>
      </div>
    );
  }
    
    
    return(
      <div id="whc_home_one">
        <header id="header" className="whc_header_main_area headroom">
          <section className="whc_middle_toolbar">
            <div className="whc_main_container">
              <div className="row">
                <div className="col-auto mr-auto">
                  <div className="whc_toolbar_address">
                    <a href="#">
                      <i className="fa fa-headphones"></i>
                      <span>24/7 Support</span>
                    </a>
                    <a href="#">
                      <i className="fa fa-mobile"></i>
                      <span>+78 456 937 230</span>
                    </a>
                    <a href="#">
                      <i className="fa fa-envelope"></i>
                      <span>info@electricity.de</span>
                    </a>
                  </div>
                </div>
                <div className="col-auto">
                  <div className="whc_toolbar_main_login">
                    <a
                      href="#"
                      data-toggle="modal"
                      data-target="#bd_example_modal_lg3"
                    >
                      <i className="fa fa-user"></i>
                      Login
                    </a>
                    <a
                      href="#"
                      data-toggle="modal"
                      data-target="#bd_example_modal_lg4"
                    >
                      <i className="fa fa-sign-in"></i>
                      Signup
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section className="whc_header_nav home_main_nav">
            <div className="whc_main_container">
              <div className="row">
                <div className="col-auto mr-auto">
                  <div className="whc_header_logo_two">
                    <a href="index.html">
                      <img src="images/svg/ECKERT.svg" alt="" />
                    </a>
                  </div>
                </div>
                <div className="col-auto mr-auto">
                  <nav className="whc_mainmenu">
                    <ul>
                      <li className="current_page_item">
                        <a href="">
                          <i>Home</i>
                        </a>
                      </li>
                      <li>
                        <a href="">
                          Tariffs<i className="fa fa-angle-down"></i>
                        </a>
                        <ul className="megamenu-content">
                          <li>
                            <div className="row">
                              <div className="col-menu col-md-3">
                                <a href="cloud-hosting.html">
                                  <h6 className="title">Basic</h6>
                                </a>
                                <div className="content">
                                  <span className="flaticon-hosting"></span>
                                  <h5>
                                    Starting from <b>20 ct / kwh</b>
                                  </h5>
                                  <a
                                    href="cloud-hosting.html"
                                    className="button btn btn-outline"
                                  >
                                    Buy Now
                                  </a>
                                </div>
                              </div>
                            </div>

                            <div className="col-menu col-md-3">
                              <a href="dedicated-hosting.html">
                                <h6 className="title">Standard</h6>
                              </a>
                              <div className="content">
                                <span className="flaticon-server"></span>
                                <h5>
                                  Starting from <b>30 ct / kwh</b>
                                </h5>
                                <a
                                  href="dedicated-hosting.html"
                                  className="button btn btn-outline"
                                >
                                  Buy Now
                                </a>
                              </div>
                            </div>

                            <div className="col-menu col-md-3">
                              <a href="reseller-hosting.html">
                                <h6 className="title">Premium</h6>
                              </a>
                              <div className="content">
                                <span className="flaticon-server-1"></span>
                                <h5>
                                  Starting from <b>40 ct / kwh</b>
                                </h5>
                                <a
                                  href="reseller-hosting.html"
                                  className="button btn btn-outline"
                                >
                                  Buy Now
                                </a>
                              </div>
                            </div>

                            <div className="col-menu col-md-3">
                              <a href="reseller-hosting.html">
                                <h6 className="title">Green</h6>
                              </a>
                              <div className="content">
                                <span className="flaticon-server-1"></span>
                                <h5>
                                  Starting from <b>50 ct / kwh</b>
                                </h5>
                                <a
                                  href="reseller-hosting.html"
                                  className="button btn btn-outline"
                                >
                                  Buy Now
                                </a>
                              </div>
                            </div>
                          </li>
                        </ul>
                      </li>
                    </ul>
                  </nav>
                </div>
                <div className="col-auto">
                  <div className="whc_header_main_btn">
                    <a href="contact.html" className="whc_btn_three">
                      Contact us
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </header>

        <section className="whc_banner_main_area">
          <div
            className="swiper-container whc_banner_two"
            data-swiper-config='{"loop": true, "effect": "slide", "speed": 800, "autoplay": 5000, "grabCursor": true, "slidesPerView":1}'
          >
            <div className="swiper-wrapper">
              <div
                className="swiper-slide"
                data-bg-image="images/svg/banner_main.svg"
                data-parallax="image"
              >
                <div className="whc_main_container">
                  <div className="row">
                    <div className="col-xl-5 col-sm-6">
                      <div className="whc_banner_main_img">
                        <img
                          data-animate="zoomIn"
                          data-delay="1.8s"
                          data-duration="1.2s"
                          src="images/main/electricity_one.jpg"
                          alt=""
                        />
                      </div>
                    </div>
                    <div className="col-xl-6 offset-xl-1 col-sm-6">
                      <div className="whc_swiper-slide-main">
                        <div className="whc_banner_main_title">
                          <span data-animate="fadeInDown">Eckert</span>
                          <h2
                            data-animate="flipInX"
                            data-delay="0.8s"
                            data-duration="1.0s"
                          >
                            Your Electricity <br />
                            Provider
                          </h2>
                        </div>
                        <div
                          className="whc_banner_main_two_btn"
                          data-animate="fadeInLeft"
                          data-delay="1.2s"
                          data-duration="1.0s"
                        >
                          <a href="#" className="whc_btn_main">
                            Contact us
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                className="swiper-slide"
                data-bg-image="images/svg/banner_main_two.svg"
                data-parallax="image"
              >
                <div className="whc_main_container">
                  <div className="row">
                    <div className="col-xl-5 offset-xl-2 col-sm-6">
                      <div className="whc_swiper-slide-main">
                        <div className="whc_banner_main_title">
                          <span data-animate="fadeInDown">Eckert</span>
                          <h2
                            data-animate="flipInX"
                            data-delay="0.8s"
                            data-duration="1.0s"
                          >
                            Your Cheap <br />
                            Electricity
                          </h2>
                        </div>
                        <div
                          className="whc_banner_main_two_btn"
                          data-animate="fadeInLeft"
                          data-delay="1.2s"
                          data-duration="1.0s"
                        >
                          <a href="#" className="whc_btn_main">
                            Contact us
                          </a>
                        </div>
                      </div>
                    </div>
                    <div className="col-xl-4 col-sm-6">
                      <div className="whc_banner_main_img">
                        <img
                          data-animate="zoomIn"
                          data-delay="1.8s"
                          data-duration="1.2s"
                          src="images/main/electricity_two.jpg"
                          alt=""
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="whc_service_area whc_service_main_area">
          <div className="whc_main_container">
            <div className="whc_section_title">
              <h3>OUR SERVICES</h3>
              <p>
                Our electricity provider services ensure affordable rates,
                reliable energy supply, and eco-friendly options for a
                sustainable home.
              </p>
            </div>
            <div className="row">
              <div className="col-xl-9 col-md-12">
                <div className="row">
                  <div className="col-xl-6 col-md-6">
                    <div className="whc_single_service">
                      <div className="whc_single_service_icon">
                        <span className="flaticon-database-1"></span>
                      </div>
                      <div className="whc_single_service_desc">
                        <h3>Experience</h3>
                        <p>
                          Experience top-notch customer service, flexible
                          contract terms, and innovative solutions for your
                          energy needs with our electricity provider services.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-6 col-md-6">
                    <div className="whc_single_service">
                      <div className="whc_single_service_icon">
                        <span className="flaticon-database-1"></span>
                      </div>
                      <div className="whc_single_service_desc">
                        <h3>Electricity</h3>
                        <p>
                          Our electricity provider services offer transparency,
                          simple tariff options, and a variety of deals to
                          optimize your individual energy consumption.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-6 col-md-6">
                    <div className="whc_single_service">
                      <div className="whc_single_service_icon">
                        <span className="flaticon-database-1"></span>
                      </div>
                      <div className="whc_single_service_desc">
                        <h3>Provider</h3>
                        <p>
                          Rely on our electricity provider services for stable
                          energy supply, fair prices, and additional services
                          that cater to your needs effectively.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-6 col-md-6">
                    <div className="whc_single_service">
                      <div className="whc_single_service_icon">
                        <span className="flaticon-database-1"></span>
                      </div>
                      <div className="whc_single_service_desc">
                        <h3>Energy</h3>
                        <p>
                          Explore a variety of sustainable energy sources,
                          flexible contract durations, and excellent customer
                          support with our electricity provider services.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-xl-3">
                <div className="whc_service_bg_main_right">
                  <img src="images/main/electricity_two.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
        </section>

        <section
          className="whc_counter_two_area whc_counter_main_area"
          data-parallax="image"
          data-bg-image="images/whc-counter-bg.jpg"
        >
          <div className="whc_main_container">
            <div className="row">
              <div className="col-xl-3 col-lg-3 col-md-6 col-6">
                <div className="whc_single_counter">
                  <div className="whc_single_counter_desc">
                    <div className="whc_single_icon">
                      <span className="flaticon-group"></span>
                    </div>
                    <div className="whc_single_count">
                      <h2>
                        <span className="counter">670 </span>
                        <span>Customers</span>
                        <b>REGISTERED</b>
                      </h2>
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-xl-3 col-lg-3 col-md-6 col-6">
                <div className="whc_single_counter">
                  <div className="whc_single_icon">
                    <span className="flaticon-group"></span>
                  </div>
                  <div className="whc_single_count">
                    <h2>
                      <span className="counter">980 </span>
                      <span>People</span>
                      <b>HAPPY CLIENTS</b>
                    </h2>
                  </div>
                </div>
              </div>
              <div className="col-xl-3 col-lg-3 col-md-6 col-6">
                <div className="whc_single_counter">
                  <div className="whc_single_icon">
                    <span className="flaticon-group"></span>
                  </div>
                  <div className="whc_single_count">
                    <h2>
                      <span className="counter">250 </span>
                      <span>Employee</span>
                      <b>available</b>
                    </h2>
                  </div>
                </div>
              </div>
              <div className="col-xl-3 col-lg-3 col-md-6 col-6">
                <div className="whc_single_counter">
                  <div className="whc_single_icon">
                    <span className="flaticon-group"></span>
                  </div>
                  <div className="whc_single_count">
                    <h2>
                      <span className="counter">275 </span>
                      <span>Euro</span>
                      <b>Discount</b>
                    </h2>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="whc_terminator_area whc_megahost_fundamental">
          <div className="whc_main_container">
            <div className="row">
              <div className="col-xl-6 col-lg-5 col-md-12">
                <div className="whc_terminator_right">
                  <img src="images/main/electricity_one.jpg" alt="" />
                </div>
              </div>
              <div className="col-xl-6 col-lg-7 col-md-12">
                <div className="whc_terminator_content clearfix">
                  <h2>Electricity</h2>
                  <p>
                    Electricity powers our homes, providing essential energy for
                    lighting, appliances, and technology, revolutionizing the
                    way we live and work in modern society
                  </p>
                  <div className="whc_terminator_list">
                    <ul>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Supply
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Sources
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Transmission
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Billing
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Support
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Tariffs
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Renewables
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Maintenance
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Compliance
                      </li>
                      <li>
                        <i className="fa fa-paper-plane-o"></i>
                        Innovation
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section
          className="whc_client_feedback_area"
          data-bg-image="images/whc-feedback-bg.jpg"
          data-parallax="image"
        >
          <div className="whc_main_container">
            <div className="whc_section_title">
              <h3>OUR CLIENTS & FEEDBACK</h3>
            </div>
            <div
              className="swiper-container"
              data-swiper-config='{"loop": true, "effect": "slide", "speed": 800, "autoplay": 5000, "grabCursor": true, "slidesPerView":1}'
            >
              <div className="swiper-wrapper">
                <div className="swiper-slide">
                  <div className="whc_main_container">
                    <div className="row">
                      <div className="col-lg-8 col-sm-12 offset-sm-0 offset-lg-2">
                        <div className="whc_sn_feedback">
                          <i className="fa fa-quote-right"></i>
                          <blockquote>
                            I've been a customer of XYZ Electricity for three
                            years now, and I couldn't be happier. Their customer
                            service is outstanding - whenever I've had an issue,
                            they've responded promptly and resolved it
                            efficiently. Moreover, their rates are competitive,
                            and the transition to renewable energy options was
                            seamless. I highly recommend them to anyone looking
                            for a reliable electricity provider.
                          </blockquote>
                          <img src="images/whc-client-feedback.jpg" alt="" />
                          <div className="whc_client_desig">
                            <h3>
                              Karl Lauterbacher<span>Customer</span>
                            </h3>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="swiper-button-next">
                <i className="fa fa-angle-left"></i>
              </div>
              <div className="swiper-button-prev">
                <i className="fa fa-angle-right"></i>
              </div>
            </div>
          </div>
        </section>

        <section className="whc_branding_area whc_main_branding_area">
          <div className="whc_main_container">
            <div
              className="swiper-container whc_brand_container"
              data-swiper-config='{"loop": true, "effect": "slide", "autoplay": 5000, "speed": 800, "slidesPerView":5, "breakpoints": {"1600": { "slidesPerView": 4 }, "1200": { "slidesPerView": 3 }, "991": { "slidesPerView": 2 }, "767": { "slidesPerView": 1 }}}'
            >
              <div className="swiper-wrapper">
                <div className="swiper-slide">
                  <div className="whc_sn_brand">
                    <svg>
                      <rect x="5" y="5" rx="0" width="100%" height="110"></rect>
                    </svg>
                    <img src="images/main/electricity_three.jpg" alt="" />
                  </div>
                </div>
                <div className="swiper-slide">
                  <div className="whc_sn_brand">
                    <svg>
                      <rect x="5" y="5" rx="0" width="100%" height="110"></rect>
                    </svg>
                    <img src="images/main/electricity_four.jpg" alt="" />
                  </div>
                </div>
                <div className="swiper-slide">
                  <div className="whc_sn_brand">
                    <svg>
                      <rect x="5" y="5" rx="0" width="100%" height="110"></rect>
                    </svg>
                    <img src="images/main/electricity_five.jpg" alt="" />
                  </div>
                </div>
                <div className="swiper-slide">
                  <div className="whc_sn_brand">
                    <svg>
                      <rect x="5" y="5" rx="0" width="100%" height="110"></rect>
                    </svg>
                    <img src="images/main/electricity_six.jpg" alt="" />
                  </div>
                </div>
                <div className="swiper-slide">
                  <div className="whc_sn_brand">
                    <svg>
                      <rect x="5" y="5" rx="0" width="100%" height="110"></rect>
                    </svg>
                    <img src="images/main/electricity_four.jpg" alt="" />
                  </div>
                </div>
                <div className="swiper-slide">
                  <div className="whc_sn_brand">
                    <svg>
                      <rect x="5" y="5" rx="0" width="100%" height="110"></rect>
                    </svg>
                    <img src="images/main/electricity_one.jpg" alt="" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="whc_subscribe_area light_blue">
          <div className="whc_main_container">
            <div className="row">
              <div className="col-xl-6 col-md-6">
                <div className="whc_subscribe_support">
                  <a href="#">
                    <span className="flaticon-customer-support"></span>
                    <b>
                      Support
                      <span>24X7</span>
                    </b>
                  </a>
                  <a href="#">
                    <span className="flaticon-live-chat"></span>
                    <b>
                      TALK
                      <span>LIVE CHAT</span>
                    </b>
                  </a>
                </div>
              </div>
              <div className="col-xl-6 col-md-6">
                <div className="whc_subscribe_get-start">
                  <h3>Do you have any questions?</h3>
                  <a href="#">Contact us</a>
                </div>
              </div>
            </div>
          </div>
        </section>

        <footer className="whc_footer_area">
          <section className="whc_footer_top">
            <div className="whc_main_container">
              <div className="row">
                <div className="col-xl-3 col-lg-3 col-md-6 col-sm-6">
                  <div className="whc_widget">
                    <div className="whc_widget_top">
                      <div className="whc_widget_ft_logo">
                        <a href="index.html">
                          <img src="images/svg/ECKERT.svg" alt="" />
                        </a>
                      </div>
                      <div className="whc_widget_desc">
                        <p>
                          1-9 Coblitzallee
                          <br /> 68163, Mannheim.
                        </p>
                        <div className="whc_widget_add">
                          <a href="#">
                            <i className="fa fa-phone"></i>
                            <span>
                              <b>Phone :</b> +78 456 937 230
                            </span>
                          </a>
                          <a href="#">
                            <i className="fa fa-envelope"></i>
                            <span>
                              <b>Mail :</b> info@electricity.de{" "}
                            </span>
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="col-xl-3 col-lg-3 offset-lg-0 col-md-6 col-sm-6">
                  <div className="whc_widget whc_top">
                    <div className="whc_widget_title">
                      <h3>Tariffs</h3>
                    </div>
                    <div className="whc_widget_list">
                      <ul>
                        <li>
                          <a href="#">Tariff Basic</a>
                        </li>
                        <li>
                          <a href="#">Tariff Standard</a>
                        </li>
                        <li>
                          <a href="#">Tariff Premium</a>
                        </li>
                        <li>
                          <a href="#">Tariff Green</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div className="col-xl-3 col-lg-3 offset-lg-0 col-md-6 col-sm-6">
                  <div className="whc_widget whc_top">
                    <div className="whc_widget_title">
                      <h3>Ressources</h3>
                    </div>
                    <div className="whc_widget_list">
                      <ul>
                        <li>
                          <a href="#">Electricity Report 2023</a>
                        </li>
                        <li>
                          <a href="#">Electricity Report 2022</a>
                        </li>
                        <li>
                          <a href="#">Electricity Report 2021</a>
                        </li>
                        <li>
                          <a href="#">Electricity Report 2020</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div className="col-xl-3 col-lg-3 offset-lg-0 col-md-6 col-sm-6">
                  <div className="whc_widget whc_top">
                    <div className="whc_widget_title">
                      <h3>Legal</h3>
                    </div>
                    <div className="whc_widget_list">
                      <ul>
                        <li>
                          <a href="#">Imprint</a>
                        </li>
                        <li>
                          <a href="#">Privacy Policy</a>
                        </li>
                        <li>
                          <a href="#">Cookies</a>
                        </li>
                        <li>
                          <a href="#">AGB</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section className="whc_footer_bottom">
            <div className="whc_main_container">
              <div className="whc_copyright">
                <p>
                  Copyright 2023 © <a href="#">Eckert</a>. All Rights Reserved.
                </p>
              </div>
            </div>
          </section>
        </footer>

        <div className="backtotop">
          <i className="fa fa-angle-up backtotop_btn"></i>
        </div>

        <div
          className="modal fade"
          id="bd_example_modal_lg3"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div className="modal-dialog modal-lg">
            <div className="modal-content">
              <div className="container">
                <div className="row">
                  <div className="col-md-12">
                    <div className="whc_modal_tab_section">
                      <ul className="nav whc_modal_tab_menu" role="tablist">
                        <li>
                          <a
                            className="active"
                            id="login-tab"
                            data-toggle="tab"
                            href="#login"
                            role="tab"
                            aria-controls="login"
                            aria-expanded="true"
                          >
                            Sign In
                          </a>
                        </li>
                        <li>
                          <a
                            className=""
                            id="sign-up-tab"
                            data-toggle="tab"
                            href="#sign-up"
                            role="tab"
                            aria-controls="sign-up"
                          >
                            Sign up
                          </a>
                        </li>
                      </ul>
                      <div className="tab-content whc_modal_tab_content">
                        <div
                          className="tab-pane fade show active"
                          id="login"
                          role="tabpanel"
                          aria-labelledby="login-tab"
                        >
                          <div className="row">
                            <div className="col-md-12 col-lg-6 whc_brand_description_area">
                              <img
                                src="images/svg/ECKERT.svg"
                                className="img-fluid"
                                alt=""
                              />
                            </div>
                            <div className="col-md-12 col-lg-6">
                              <div className="whc_login_section">
                                <div className="whc_login_form">
                                  <form action="#">
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        id="exampleInputEmail-login"
                                        placeholder="Enter your E-Mail"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="password"
                                        id="exampleInputPassword-login-pass-2"
                                        placeholder="Password"
                                      />
                                    </div>
                                    <button type="submit" className="sign_in">
                                      Sign in
                                    </button>

                                    <div className="whc_policy">
                                      <p>
                                        By Continuing. I confirm that i have
                                        read and userstand the{" "}
                                        <a href="#">terms of uses</a> and{" "}
                                        <a href="#">Privacy Policy</a>. Don’t
                                        have an account?{" "}
                                        <a href="#" className="black-color">
                                          <strong>
                                            <u>Sign up</u>
                                          </strong>
                                        </a>
                                      </p>
                                    </div>
                                  </form>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div
                          className="tab-pane fade"
                          id="sign-up"
                          role="tabpanel"
                          aria-labelledby="sign-up-tab"
                        >
                          <div className="row">
                            <div className="col-lg-6 col-md-6 whc_brand_description_area whc_signup">
                              <img
                                src="images/svg/ECKERT.svg"
                                className="img-fluid"
                                alt=""
                              />
                            </div>
                            <div className="col-lg-6 col-md-12">
                              <div className="whc_login_section">
                                <div className="whc_login_form">
                                  <form action="#">
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        className="form-control"
                                        id="exampleInputclassname1"
                                        placeholder="First className"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        className="form-control"
                                        id="exampleInputclassname2"
                                        placeholder="Last className"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        className="form-control"
                                        id="exampleInputEmail-sign-up"
                                        placeholder="Enter you E-mail"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="password"
                                        className="form-control"
                                        id="exampleInputPassword-login-pass"
                                        placeholder="*** *** ***"
                                      />
                                    </div>
                                    <button type="submit" className="sign_up">
                                      Sign up
                                    </button>

                                    <div className="whc_policy">
                                      <p>
                                        By Continuing. I confirm that i have
                                        read and userstand the{" "}
                                        <a href="#">terms of uses</a> and{" "}
                                        <a href="#">Privacy Policy</a>
                                        Don’t have an account?{" "}
                                        <a href="#" className="black-color">
                                          <strong>
                                            <u>Sign up</u>
                                          </strong>
                                        </a>
                                      </p>
                                    </div>
                                  </form>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div
          className="modal fade"
          id="bd_example_modal_lg4"
          tabindex="-1"
          role="dialog"
          aria-hidden="true"
        >
          <div className="modal-dialog modal-lg">
            <div className="modal-content">
              <div className="container">
                <div className="row">
                  <div className="col-xl-12">
                    <div className="whc_modal_tab_section">
                      <ul className="nav whc_modal_tab_menu" role="tablist">
                        <li>
                          <a
                            className=""
                            data-toggle="tab"
                            href="#login_two"
                            role="tab"
                            aria-controls="login"
                            aria-expanded="true"
                          >
                            Sign In
                          </a>
                        </li>
                        <li>
                          <a
                            className="active"
                            data-toggle="tab"
                            href="#sign_up_two"
                            role="tab"
                            aria-controls="sign-up"
                          >
                            Sign up
                          </a>
                        </li>
                      </ul>
                      <div className="tab-content whc_modal_tab_content">
                        <div
                          className="tab-pane fade"
                          id="login_two"
                          role="tabpanel"
                          aria-labelledby="login-tab"
                        >
                          <div className="row">
                            <div className="col-md-12 col-lg-6 whc_brand_description_area">
                              <img
                                src="images/svg/ECKERT.svg"
                                className="img-fluid"
                                alt=""
                              />
                            </div>
                            <div className="col-md-12 col-lg-6">
                              <div className="whc_login_section">
                                <div className="whc_login_form">
                                  <form action="#">
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        placeholder="Enter your E-Mail"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="password"
                                        placeholder="Password"
                                      />
                                    </div>
                                    <button type="submit" className="sign_in">
                                      Sign in
                                    </button>

                                    <div className="whc_login_form_check">
                                      <label className="whc_form_check_">
                                        <input
                                          type="checkbox"
                                          className="form-check-input"
                                        />
                                        Save this password
                                      </label>
                                    </div>
                                    <div className="whc_policy">
                                      <p>
                                        By Continuing. I confirm that i have
                                        read and userstand the{" "}
                                        <a href="#">terms of uses</a> and{" "}
                                        <a href="#">Privacy Policy</a>.
                                      </p>
                                    </div>
                                  </form>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div
                          className="tab-pane fade active show"
                          id="sign_up_two"
                          role="tabpanel"
                          aria-labelledby="sign-up-tab"
                        >
                          <div className="row">
                            <div className="col-md-12 col-lg-6 whc_brand_description_area whc_signup">
                              <img
                                src="images/svg/ECKERT.svg"
                                className="img-fluid"
                                alt=""
                              />
                            </div>
                            <div className="col-md-12 col-lg-6 ">
                              <div className="whc_login_section">
                                <div className="whc_login_form">
                                  <form action="#">
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        className="form-control"
                                        placeholder="First className"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Last className"
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="text"
                                        className="form-control"
                                        placeholder="Enter you email ..."
                                      />
                                    </div>
                                    <div className="whc_login_form_group">
                                      <input
                                        type="password"
                                        className="form-control"
                                        placeholder="*** *** ***"
                                      />
                                    </div>
                                    <button type="submit" className="sign_up">
                                      Sign up
                                    </button>

                                    <div className="whc_policy">
                                      <p>
                                        By Continuing. I confirm that i have
                                        read and userstand the{" "}
                                        <a href="#">terms of uses</a> and{" "}
                                        <a href="#">Privacy Policy</a>.
                                      </p>
                                    </div>
                                  </form>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
}

export default App;
