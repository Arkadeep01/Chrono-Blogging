import { useState, useEffect } from "react";
import Header from "../partials/header";
import Footer from "../partials/footer";
import StorySection from "../../components/storySection";
import Search from "../../components/Search";
import apiInstance from "../../utils/axios";
import { fetchAllPages } from "../../utils/fetchAllPages";

const SECTION_LIMIT = 6;

function StoriesPage() {
  const [posts, setPosts] = useState([]);
  const [filteredPosts, setFilteredPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadPosts = async () => {
      try {
        setLoading(true);
        const data = await fetchAllPages(apiInstance, "post/lists/");
        setPosts(data);
        setFilteredPosts(data);
      } catch (err) {
        console.error("Failed to load posts:", err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadPosts();
  }, []);

  const trendingPosts = [...filteredPosts].sort((a, b) => {
    const scoreA = (a.views || 0) + (a.Likes?.length || 0) * 3;
    const scoreB = (b.views || 0) + (b.Likes?.length || 0) * 3;
    return scoreB - scoreA;
  }).slice(0, SECTION_LIMIT);

  const usedIds = new Set(trendingPosts.map((p) => p.id));

  const popularPosts = [...filteredPosts]
    .filter((p) => !usedIds.has(p.id))
    .sort((a, b) => (b.views || 0) - (a.views || 0))
    .slice(0, SECTION_LIMIT);
  popularPosts.forEach((p) => usedIds.add(p.id));

  const latestPosts = [...filteredPosts]
    .filter((p) => !usedIds.has(p.id))
    .sort((a, b) => new Date(b.date) - new Date(a.date))
    .slice(0, SECTION_LIMIT);
  
  const allStoriesPosts = [...filteredPosts].sort(
    (a, b) => new Date(b.date) - new Date(a.date)
  );

  if (loading) {
    return (
      <>
        <Header />
        <div className="container py-5 text-center">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3">Loading stories...</p>
        </div>
        <Footer />
      </>
    );
  }

  if (error) {
    return (
      <>
        <Header />
        <div className="container py-5 text-center">
          <p className="text-danger">Failed to load stories: {error}</p>
        </div>
        <Footer />
      </>
    );
  }

  return (
    <>
      <Header />
      <div style={{ minHeight: '100vh', backgroundColor: '#f8f9fa' }}>
        <div className="container pt-4">
          <Search posts={posts} onFilter={setFilteredPosts} />
        </div>
        
        {filteredPosts.length === 0 ? (
          <div className="container py-5 text-center">
            <p>No stories found</p>
          </div>
        ) : (
          <>
            <StorySection title="Trending Stories" posts={trendingPosts} maxPosts={6} />
            <StorySection title="Popular Stories" posts={popularPosts} maxPosts={6} />
            <StorySection title="Latest Stories" posts={latestPosts} maxPosts={6} />
            <StorySection title="All Stories" posts={allStoriesPosts} cardsOnly={true} />
          </>
        )}
      </div>
      <Footer />
    </>
  );
}

export default StoriesPage;
