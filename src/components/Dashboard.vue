<template>
  <div class="dashboard">
    <h2>Dashboard</h2>
    <div class="stats">
      <div class="stat-card" v-for="stat in stats" :key="stat.id">
        <h3>{{ stat.title }}</h3>
        <p class="value">{{ stat.value }}</p>
      </div>
    </div>
    <div class="items">
      <h3>Recent Items</h3>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }} - {{ item.status }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const stats = ref([
  { id: 1, title: 'Total Users', value: '1,234' },
  { id: 2, title: 'Active Projects', value: '56' },
  { id: 3, title: 'Tasks Completed', value: '892' },
  { id: 4, title: 'Revenue', value: '$45,678' }
])

const items = ref([
  { id: 1, name: 'Project Alpha', status: 'In Progress' },
  { id: 2, name: 'Project Beta', status: 'Completed' },
  { id: 3, name: 'Project Gamma', status: 'Planning' },
  { id: 4, name: 'Project Delta', status: 'On Hold' }
])
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.stat-card h3 {
  color: #666;
  margin-bottom: 10px;
  font-size: 1rem;
}

.value {
  font-size: 1.5rem;
  font-weight: bold;
  color: #2c3e50;
  margin: 0;
}

.items {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.items h3 {
  margin-bottom: 15px;
  color: #2c3e50;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

li:last-child {
  border-bottom: none;
}
</style>