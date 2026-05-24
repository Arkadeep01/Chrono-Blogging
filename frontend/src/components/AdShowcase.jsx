import { Link } from "react-router-dom";

function AdShowcase() {
  return (
    <section className="home-ad-section">
      <div className="container">
        <div className="home-ad-shell">
          <div className="home-ad-copy">
            <p className="home-ad-label">Sponsored</p>
            <h3>Launch Your Brand In Front Of Curious Readers</h3>
            <p>
              Promote your product, course, or newsletter with premium placement
              inside stories people actually read.
            </p>
            <Link to="/contact/" className="home-ad-btn">
              Advertise With Us
            </Link>
          </div>
          <div className="home-ad-stats">
            <div>
              <strong>120K+</strong>
              <span>Monthly impressions</span>
            </div>
            <div>
              <strong>8.2%</strong>
              <span>Average engagement</span>
            </div>
            <div>
              <strong>Tech + Culture</strong>
              <span>Audience focus</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default AdShowcase;
