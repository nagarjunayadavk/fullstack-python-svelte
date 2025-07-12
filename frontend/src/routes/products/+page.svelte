<script>
  import { onMount } from 'svelte';

  let products = [];

  onMount(async () => {
    try {
      const res = await fetch('http://localhost:8000/products');
      if (res.ok) {
        products = await res.json();
      } else {
        console.error('Failed to load products');
      }
    } catch (err) {
      console.error('Error fetching products:', err);
    }
  });
</script>

<h1 class="text-2xl font-bold mb-4">Product List</h1>

{#if products.length > 0}
  <div class="overflow-x-auto">
    <table class="min-w-full table-auto border border-gray-200 rounded">
      <thead class="bg-gray-100 text-gray-700">
        <tr>
          <th class="px-4 py-2 border">ID</th>
          <th class="px-4 py-2 border">Name</th>
          <th class="px-4 py-2 border">Description</th>
          <th class="px-4 py-2 border">Price (₹)</th>
          <th class="px-4 py-2 border">Quantity</th>
        </tr>
      </thead>
      <tbody>
        {#each products as product}
          <tr class="hover:bg-gray-50">
            <td class="px-4 py-2 border">{product.id}</td>
            <td class="px-4 py-2 border">{product.name}</td>
            <td class="px-4 py-2 border">{product.description}</td>
            <td class="px-4 py-2 border">{product.price}</td>
            <td class="px-4 py-2 border">{product.quantity}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{:else}
  <p class="text-gray-500">No products available.</p>
{/if}
