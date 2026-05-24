function UserReviews() {
  const reviews = [
    {
      id: 1,
      name: "Aarav Sen",
      role: "Frontend Developer",
      quote:
        "This platform made my reading habit consistent again. The curation quality is strong and practical.",
    },
    {
      id: 2,
      name: "Maya Kapoor",
      role: "Product Designer",
      quote:
        "I discovered writers here who break down complex ideas without fluff. The category filtering is super useful.",
    },
    {
      id: 3,
      name: "Ritvik Das",
      role: "Startup Founder",
      quote:
        "Curious Chronicle gives me clear, high-signal reads in one place. I usually save 3-4 posts every week.",
    },
  ];

  return (
    <section className="home-reviews-section">
      <div className="container">
        <div className="home-reviews-header">
          <p>Reader Voice</p>
          <h3>What Our Community Says</h3>
        </div>
        <div className="home-reviews-grid">
          {reviews.map((review) => (
            <article key={review.id} className="home-review-card">
              <p className="home-review-quote">"{review.quote}"</p>
              <div className="home-review-author">
                <strong>{review.name}</strong>
                <span>{review.role}</span>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export default UserReviews;
