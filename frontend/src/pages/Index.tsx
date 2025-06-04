import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import HeroSection from '@/components/HeroSection';
import ClassSelector from '@/components/ClassSelector';
import SubjectsSection from '@/components/SubjectsSection';
import FeaturesSection from '@/components/FeaturesSection';
import DashboardPreview from '@/components/DashboardPreview';

const Index = () => {
  const location = useLocation();
  const [djangoMessage, setDjangoMessage] = useState('');

  useEffect(() => {
    // Scroll logic
    if (location.state?.scrollToSubjects) {
      const subjectsSection = document.getElementById('subjects');
      if (subjectsSection) {
        subjectsSection.scrollIntoView({ behavior: 'smooth' });
      }
    }

    // ✅ Fetch message from Django API

  }, [location]);

  return (
    <div className="min-h-screen">
         <div className="text-center fixed 4 left-1/2 transform -translate-x-1/2 bg-red-700 text-white font-extrabold px-8 py-3 rounded-md shadow-lg border border-red-900 animate-pulse tracking-wide">
  🚧 Site is Under Development 🚧 
</div>



      <HeroSection />

      {/* ✅ Django Message */}
      <div className="text-center mt-6 text-blue-700 font-semibold animate-fade-in">
        {djangoMessage && `📡 Message from backend: ${djangoMessage}`}
      </div>

      <ClassSelector />
      <SubjectsSection />
      <FeaturesSection />
      <DashboardPreview />

      {/* Footer */}
      <footer className="bg-gradient-to-r from-eduplay-purple via-eduplay-blue to-eduplay-green py-12 animate-fade-in">
        <div className="container mx-auto px-4 text-center">
          <div className="text-white space-y-4">
            <h3 className="text-3xl font-bold animate-bounce-gentle">247School</h3>
            <p className="text-lg opacity-90 animate-slide-in-right">Learning 24/7, One Lesson at a Time! 🌟</p>
            <div className="flex justify-center space-x-6 text-4xl">
              <span className="animate-bounce-gentle">🎓</span>
              <span className="animate-wiggle">📚</span>
              <span className="animate-float">⭐</span>
              <span className="animate-scale-bounce">🏆</span>
              <span className="animate-pulse">🚀</span>
            </div>
            <p className="text-sm opacity-75 mt-8 animate-fade-in delay-500">
              © 2024 247School. Designed with ❤️ for young learners everywhere.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Index;
