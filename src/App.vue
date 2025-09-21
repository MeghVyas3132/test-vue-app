<script setup>
import { ref } from 'vue'
import Dashboard from './components/Dashboard.vue'

const tabs = ['Dashboard', 'About']
const currentTab = ref('Dashboard')
</script>

<template>
  <div class="app">
    <header>
      <img src="/vite.svg" class="logo" alt="Vite logo" />
      <h1>Vue.js Test Application</h1>
    </header>
    <nav>
      <button 
        v-for="tab in tabs" 
        :key="tab"
        :class="{ active: currentTab === tab }"
        @click="currentTab = tab"
      >
        {{ tab }}
      </button>
    </nav>
    <main>
      <Dashboard v-if="currentTab === 'Dashboard'" />
      <div v-else-if="currentTab === 'About'" class="about">
        <h2>About This App</h2>
        <p>This is a test Vue.js application created with Vite. It demonstrates:</p>
        <ul>
          <li>Vue 3 Composition API</li>
          <li>Component creation and usage</li>
          <li>State management with refs</li>
          <li>Conditional rendering</li>
          <li>List rendering</li>
          <li>Event handling</li>
          <li>Styling with scoped CSS</li>
        </ul>
      </div>
    </main>
  </div>
</template>

<style scoped>
.app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
}

.logo {
  height: 40px;
}

h1 {
  margin: 0;
  color: #2c3e50;
}

nav {
  margin-bottom: 20px;
}

button {
  background: none;
  border: none;
  padding: 10px 20px;
  margin-right: 10px;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #f0f0f0;
}

button.active {
  background-color: #42b883;
  color: white;
}

.about {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.about ul {
  padding-left: 20px;
}

.about li {
  margin: 10px 0;
  color: #666;
}
</style>
