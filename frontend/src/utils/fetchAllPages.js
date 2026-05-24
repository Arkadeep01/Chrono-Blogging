/**
 * Fetch every page from a DRF paginated list endpoint.
 * Backend default page_size is 6; we request up to 50 per page.
 */
export async function fetchAllPages(apiInstance, url, extraParams = {}) {
  let page = 1;
  let results = [];
  let hasNext = true;

  while (hasNext) {
    const res = await apiInstance.get(url, {
      params: { ...extraParams, page, page_size: 50 },
    });
    const data = res.data;

    if (Array.isArray(data)) {
      return data;
    }

    const pageResults = data?.results || [];
    results = [...results, ...pageResults];
    hasNext = Boolean(data?.next);
    page += 1;
  }

  return results;
}
