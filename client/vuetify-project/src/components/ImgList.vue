<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-col>
    </v-row>
    <v-list>
      <v-list-item v-for="(image, index) in filteredImages" :key="index">
        <v-list-item-title>Image Slot {{ index + 1 }}</v-list-item-title>
      </v-list-item>
    </v-list>
    <v-pagination
      v-model="page"
      :length="pageCount"
      @input="onPageChange"
    ></v-pagination>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      images: [],
      page: 1,
      itemsPerPage: 4,
      search: '',
    };
  },
  computed: {
    filteredImages() {
      let images = this.images;
      if (this.search) {
        images = images.filter((image) =>
          image.tags.some((tag) => tag.includes(this.search))
        );
      }
      const start = (this.page - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return images.slice(start, end);
    },
    pageCount() {
      return Math.ceil(this.images.length / this.itemsPerPage);
    },
  },
  methods: {
    async fetchData() {
      console.log('fetchData called');
      try {
        const response = await fetch('http://127.0.0.1:8000/images');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched data:', data);
        this.images = data;
      } catch (error) {
        console.error('Fetch error:', error);
      }
    },
    onPageChange() {
      window.scrollTo(0, 0);
    },
  },
  mounted() {
    console.log('Component mounted');
    this.fetchData();
  },
};
</script>

<style scoped>
/* Add any scoped styles for your component here */
</style>
