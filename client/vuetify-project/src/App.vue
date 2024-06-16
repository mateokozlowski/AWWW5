<template>
  <v-app>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field v-model="search" label="Search" append-icon="mdi-magnify"></v-text-field>
        </v-col>
        <v-col cols="12">
          <ImgList />
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import ImgList from './components/ImgList.vue';

export default {
  components: {
    ImgList
  },
  data() {
    return {
      search: '',
      items: [
        { title: 'Item 1', subtitle: 'Lorem ipsum dolor sit amet' },
        { title: 'Item 2', subtitle: 'Consectetur adipiscing elit' },
        { title: 'Item 3', subtitle: 'Sed do eiusmod tempor incididunt' }
      ]
    };
  }
};
</script>
