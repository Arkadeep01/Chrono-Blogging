import { Link } from "react-router-dom";

function CommunityCTA() {
  return (
    <section className="home-community-section">
      <div className="container">
        <div className="home-community-card">
          <div>
            <p className="home-community-label">Weekly Brief</p>
            <h3>Get 5 Best Stories Every Friday</h3>
            <p>
              Join our reader circle and receive curated links on technology,
              design, business, and modern culture.
            </p>
          </div>
          <div className="home-community-actions">
            <Link to="/register/" className="home-community-btn primary">
              Join Free
            </Link>
            <Link to="/about/" className="home-community-btn secondary">
              Learn More
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default CommunityCTA;
