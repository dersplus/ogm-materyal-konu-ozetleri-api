const axios = require('axios').default;

let text = 'Matematik'; // Arama parametreniz

axios.get('https://api.dersplus.net/ogm/konu-ozetleri/search', {
  params: {
    text: text
  }
})
.then((response) => {
  console.log(response.data);
})
.catch((error) => {
  console.error(error);
});
