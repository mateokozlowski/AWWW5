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
    <v-chip v-if="newImagesCount" color="green">
      {{ newImagesCount }} new images available
      <v-btn small @click="refreshImages">Refresh</v-btn>
    </v-chip>
    <v-list>
      <v-list-item v-for="(image, index) in filteredImages" :key="index">
        <v-list-item-title>Image Slot {{ index + 1 }}</v-list-item-title>
        <v-list-item-action>
          <v-btn @click="showImage(image.id)">Show Image</v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
    <v-pagination
      v-model="page"
      :length="pageCount"
      @input="onPageChange"
    ></v-pagination>
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="headline">Image</v-card-title>
        <v-card-text>
          <div v-if="loading">Loading...</div>
          <div v-else-if="error">{{ error }}</div>
          <div v-else>
            <div v-html="selectedImage.svg"></div>
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      images: [],
      newImagesCount: 0,
      page: 1,
      itemsPerPage: 4,
      search: '',
      dialog: false,
      selectedImage: null,
      loading: false,
      error: null,
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
        this.newImagesCount = 0;  // Reset the new images count after fetching data
      } catch (error) {
        console.error('Fetch error:', error);
      }
    },
    async checkNewImages() {
      console.log('checkNewImages called');
      try {
        const response = await fetch('http://127.0.0.1:8000/new-images');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('New images data:', data);
        this.newImagesCount += data.new_images;
      } catch (error) {
        console.error('Fetch error:', error);
      }
    },
    async refreshImages() {
      await this.fetchData();
    },
    async showImage(imageId) {
      this.dialog = true;
      this.loading = true;
      this.error = null;
      this.selectedImage = null;
      try {
        const response = await fetch(`http://127.0.0.1:8000/images/${imageId}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.selectedImage = data;
        this.loading = false;
      } catch (error) {
        this.error = 'Failed to load image';
        this.loading = false;
      }
    },
    onPageChange() {
      window.scrollTo(0, 0);
    },
  },
  mounted() {
    console.log('Component mounted');
    this.fetchData();
    this.checkNewImages();
    this.newImagesInterval = setInterval(this.checkNewImages, 2000); // Co minutę sprawdzaj nowe obrazki
  },
  beforeDestroy() {
    // Clear the interval when the component is destroyed to avoid memory leaks
    clearInterval(this.newImagesInterval);
  },
};
</script>

<style scoped>
/* Add any scoped styles for your component here */
</style>
