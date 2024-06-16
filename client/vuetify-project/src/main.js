import { createApp } from 'vue';
import App from './App.vue';

// Import Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
  components,
  directives,
});

// Create and mount the app
const app = createApp(App);
app.use(vuetify);
app.mount('#app');
