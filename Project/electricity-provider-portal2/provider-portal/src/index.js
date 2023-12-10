
import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import $ from 'jquery';
window.jQuery = $;
window.$ = $;

function Main() {
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/popper.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);

  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/popper.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/bootstrap.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/bootstrap-progressbar.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/masonry.pkgd.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/swiper.jquery.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/swiperRunner.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/headroom.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/jquery.marquee.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/rangeslider.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/waypoints.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/jquery.counterup.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/gmap3.min.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);
  
  useEffect(() => {
    const script = document.createElement('script');
    script.src = "${process.env.PUBLIC_URL}/js/main.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);

  return (
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Main />);

reportWebVitals();
