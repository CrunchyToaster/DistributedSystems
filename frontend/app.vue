<template>
  <UApp>
    <!-- Outer container to center everything -->
    <div class="min-h-screen flex flex-col items-center justify-center text-center px-4">
      <h1 class="mb-6 text-2xl font-medium tracking-tight">
        Shopping Items – Full API Test
      </h1>

      <!-- 1) FETCH ITEMS & DISPLAY LIST -->
      <section class="mb-8">
        <UButton color="primary" variant="subtle" @click="fetchItems">
          Fetch Items
        </UButton>

        <div v-if="items.length" class="mt-4">
          <ul>
            <li
              v-for="item in items"
              :key="item.id"
              class="flex items-center gap-2 justify-center mb-2"
            >
              <span>{{ item.id }} – {{ item.name }} ({{ item.quantity }})</span>
              <UButton
                color="error"
                variant="subtle"
                size="sm"
                @click="deleteItem(item.id)"
              >
                Delete
              </UButton>
            </li>
          </ul>
        </div>
        <div v-else class="mt-4">
          <p>No items yet. Click "Fetch Items" to load from the API.</p>
        </div>
      </section>

      <!-- 2) ADD or UPDATE by NAME (POST /items) -->
      <section class="mb-8 w-full max-w-sm">
        <h2 class="text-lg font-medium mb-2">Add/Update by Name</h2>
        <div class="mb-3">
          <label class="block text-left font-medium mb-1" for="createName">Name:</label>
          <input
            id="createName"
            v-model="newItem.name"
            class="border border-gray-300 px-3 py-2 w-full rounded"
            type="text"
            placeholder="e.g. Bananas"
          />
        </div>
        <div class="mb-3">
          <label class="block text-left font-medium mb-1" for="createQty">Quantity:</label>
          <input
            id="createQty"
            v-model.number="newItem.quantity"
            class="border border-gray-300 px-3 py-2 w-full rounded"
            type="number"
            min="1"
            placeholder="e.g. 5"
          />
        </div>
        <UButton color="success" variant="subtle" @click="createOrUpdateByName">
          Add/Update
        </UButton>
      </section>

      <!-- 3) UPDATE by ID (PUT /items/{id}) -->
      <section class="mb-8 w-full max-w-sm">
        <h2 class="text-lg font-medium mb-2">Update by ID</h2>
        <div class="mb-3">
          <label class="block text-left font-medium mb-1" for="updateId">Item ID:</label>
          <input
            id="updateId"
            v-model.number="updateByID.id"
            class="border border-gray-300 px-3 py-2 w-full rounded"
            type="number"
            min="1"
            placeholder="Existing item ID"
          />
        </div>
        <div class="mb-3">
          <label class="block text-left font-medium mb-1" for="updateName">Name:</label>
          <input
            id="updateName"
            v-model="updateByID.name"
            class="border border-gray-300 px-3 py-2 w-full rounded"
            type="text"
            placeholder="e.g. Bananas"
          />
        </div>
        <div class="mb-3">
          <label class="block text-left font-medium mb-1" for="updateQty">Quantity:</label>
          <input
            id="updateQty"
            v-model.number="updateByID.quantity"
            class="border border-gray-300 px-3 py-2 w-full rounded"
            type="number"
            min="1"
            placeholder="e.g. 10"
          />
        </div>
        <UButton color="success" variant="subtle" @click="updateItemByID">
          Update
        </UButton>
      </section>
    </div>
  </UApp>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// Holds the list of items
const items = ref([])

// For POST /items: Create or update by name
const newItem = ref({
  name: '',
  quantity: 1
})

// For PUT /items/{id}: Update by ID
const updateByID = ref({
  id: null,
  name: '',
  quantity: 1
})

// Base URL to your API (adjust if different)
const BASE_URL = 'https://reimagined-tribble-qg469wrqqjgh94rw-8000.app.github.dev/api/items'

// 1) GET /items
async function fetchItems() {
  try {
    const { data } = await axios.get(BASE_URL + '/')
    items.value = data
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}

// 2) POST /items -> Creates or updates an item by name
async function createOrUpdateByName() {
  try {
    // POST body: { name: "...", quantity: 5 }
    await axios.post(BASE_URL + '/', {
      name: newItem.value.name,
      quantity: newItem.value.quantity
    })
    // Refresh list so we can see changes
    fetchItems()
    // Reset form
    newItem.value = { name: '', quantity: 1 }
  } catch (error) {
    console.error('Error creating/updating item by name:', error)
  }
}

// 3) PUT /items/{id} -> Updates item by ID
async function updateItemByID() {
  try {
    if (!updateByID.value.id) {
      console.error('No ID provided for update')
      return
    }
    const { id, name, quantity } = updateByID.value
    await axios.put(BASE_URL + `/${id}/`, { name, quantity })
    // Refresh list
    fetchItems()
    // Reset form
    updateByID.value = { id: null, name: '', quantity: 1 }
  } catch (error) {
    console.error('Error updating item by ID:', error)
  }
}

// 4) DELETE /items/{id}
async function deleteItem(itemId) {
  try {
    await axios.delete(BASE_URL + `/${itemId}/`)
    fetchItems()
  } catch (error) {
    console.error('Error deleting item:', error)
  }
}
</script>
