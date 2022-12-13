window.addEventListener('DOMContentLoaded', (event) => {
   if (typeof ymaps != 'object') {
       return;
   }
   const dommap = document.querySelector('#map');
   if (!dommap) {
       return;
   }
   let lat = +dommap.dataset?.lat;
   let lng = +dommap.dataset?.lng;
   if (!lat || !lng) {
       return;
   }
   ymaps.ready(() => {
       let coords = [lat, lng];
       const map = new ymaps.Map('map', {
           center: coords,
           zoom: 13
       }, {
           searchControlProvider: 'yandex#search'
       });
       let placemark = new ymaps.Placemark(coords, {}, {
            preset: 'islands#icon',
            iconColor: '#0095b6'
       });
       map.geoObjects.add(placemark);
   });
});
