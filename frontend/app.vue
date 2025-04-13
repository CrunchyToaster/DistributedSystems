<template>
  <header>
    <h1>My Shopping App</h1>
  </header>

  <main>
    <button @click="fetchItems">Fetch Items</button>
    <div v-if="items.length">
      <h2>Items in the List</h2>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }} ({{ item.quantity }})
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No items yet. Click "Fetch Items" to load from the API.</p>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const items = ref([])

async function fetchItems() {
  try {
    const response = await axios.get('https://reimagined-tribble-qg469wrqqjgh94rw-8000.app.github.dev/api/items/')
    items.value = response.data
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}
</script>
