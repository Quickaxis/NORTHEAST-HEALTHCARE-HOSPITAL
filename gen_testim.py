data1 = [
    { "dept": "Cardio Thoracic", "review": "My father had a complex heart surgery at NEH and the outcome was beyond what we hoped for. The surgical team explained every step clearly and made us feel confident. Truly world-class care right here in Dibrugarh.", "name": "Dipankar Borthakur", "loc": "Dibrugarh, Assam" },
    { "dept": "Neurology", "review": "I had been suffering from severe migraines for years. The neurology team at NEH ran thorough diagnostics and found the root cause immediately. Within weeks of treatment I felt like myself again. Deeply grateful.", "name": "Priyanka Hazarika", "loc": "Jorhat, Assam" },
    { "dept": "Gynaecology", "review": "I delivered my baby at NEH and it was the most supported I have ever felt. The doctors and nurses were present, attentive and genuinely caring. The facility is spotless and modern. I could not have asked for better.", "name": "Raktima Saikia", "loc": "Dibrugarh, Assam" },
    { "dept": "Gastrointestinal", "review": "I travelled from Sibsagar specifically for my surgery here. The level of expertise and the quality of equipment at NEH is something I did not expect to find so close to home. Exceptional in every way.", "name": "Bhupen Gogoi", "loc": "Sibsagar, Assam" },
    { "dept": "OPD & Radiology", "review": "Fast, organised, and professional. The OPD staff were respectful and efficient. My diagnostic reports were accurate and ready quickly. This is exactly the kind of healthcare Dibrugarh needed.", "name": "Ankurita Baruah", "loc": "Dibrugarh, Assam" },
    { "dept": "Pediatrics Surgery", "review": "My son needed urgent pediatric surgery and the team at NEH responded with speed and compassion. They kept us informed throughout and my boy recovered beautifully. We are forever thankful.", "name": "Nabanita Dutta", "loc": "Tinsukia, Assam" },
    { "dept": "Dermatology", "review": "After years of trying different clinics, the dermatology department at NEH finally gave me a proper diagnosis and effective treatment. My skin condition has improved dramatically. Highly recommend.", "name": "Pallabi Neog", "loc": "Dibrugarh, Assam" },
    { "dept": "Cardiology", "review": "My mother had a cardiac emergency at 2am. The NEH emergency team responded immediately and handled everything with remarkable calmness and skill. She is fully recovered today. This hospital saved her life.", "name": "Rituraj Phukan", "loc": "Golaghat, Assam" },
    { "dept": "Ophthalmology", "review": "The ophthalmology team corrected a vision problem I had been living with for over a decade. The procedure was quick, painless, and the results were immediate. Outstanding professional care.", "name": "Minakshi Kalita", "loc": "Jorhat, Assam" },
    { "dept": "Medicine", "review": "The general medicine department took my symptoms seriously when other clinics dismissed them. Thorough testing, clear explanation, correct treatment. This is what quality healthcare looks like.", "name": "Hemanta Rajkhowa", "loc": "Dibrugarh, Assam" }
]

data2 = [
    { "dept": "Neurosurgery", "review": "I had a brain tumour diagnosis and was terrified. The neurosurgery team at NEH walked us through every option with patience and honesty. The surgery was successful and my recovery has been remarkable.", "name": "Jyotishman Borgohain", "loc": "Lakhimpur, Assam" },
    { "dept": "Plastic Surgery", "review": "I needed reconstructive surgery after an accident. The plastic surgery team at NEH delivered results that exceeded my expectations. Professional, precise, and genuinely compassionate throughout.", "name": "Chandana Handique", "loc": "Dibrugarh, Assam" },
    { "dept": "Dentistry", "review": "The dental department is modern, hygienic and very professional. Zero pain, very gentle technique, and the staff explained every procedure clearly. Best dental experience I have ever had.", "name": "Sanjeev Moran", "loc": "Dibrugarh, Assam" },
    { "dept": "Gynaecology", "review": "The prenatal care I received at NEH was exceptional. Every checkup was thorough and the doctors were always available to answer my concerns. I felt completely safe throughout my pregnancy.", "name": "Juri Tamuli", "loc": "Tinsukia, Assam" },
    { "dept": "Radiology", "review": "The radiology department has equipment I did not expect to find outside of Guwahati. Fast results, clear reports, and the radiologist explained findings in simple language. Very impressed.", "name": "Nripen Choudhury", "loc": "Sivasagar, Assam" },
    { "dept": "Gastrointestinal", "review": "My gallbladder surgery was done using minimally invasive technique and I was back home in two days. The surgical team was brilliant and post-op care was thorough. Absolutely no complaints.", "name": "Karabi Gogoi", "loc": "Dibrugarh, Assam" },
    { "dept": "Emergency", "review": "My husband was brought in with a stroke at midnight. The emergency team acted within minutes and the neurologist was there immediately. That speed of response is what saved his life. Forever grateful to NEH.", "name": "Dipali Buragohain", "loc": "Dibrugarh, Assam" },
    { "dept": "Cardiology", "review": "After my angioplasty at NEH I was back to normal life in three weeks. The cardiology team monitored every step of my recovery and were always reachable for questions. Exceptional follow-up care.", "name": "Arun Baruah", "loc": "Jorhat, Assam" },
    { "dept": "Pediatrics", "review": "My daughter had a high fever that would not break and the NEH pediatric team diagnosed and treated her within hours of arrival. The care and attention they gave her was extraordinary. We are so relieved.", "name": "Mridula Sarmah", "loc": "Golaghat, Assam" },
    { "dept": "OPD", "review": "I visited the OPD for a routine checkup and was amazed by the efficiency. No long queues, respectful staff, and a very thorough consultation. NEH has completely changed my expectations of local healthcare.", "name": "Parag Konwar", "loc": "Dibrugarh, Assam" }
]

def make_card(item):
    return f"""                <div class="w-[320px] min-h-[200px] shrink-0 bg-[rgba(255,255,255,0.06)] border border-[rgba(46,181,160,0.25)] backdrop-blur-[10px] rounded-[16px] p-[28px_24px] flex flex-col transition-all duration-300 hover:border-primary hover:scale-[1.02] overflow-hidden relative">
                    <div class="flex justify-between items-start mb-4 relative z-10">
                        <div class="text-[#FFD700] text-[18px] tracking-widest leading-none">★★★★★</div>
                        <div class="bg-primary/20 text-primary text-[11px] font-bold px-2.5 py-1 rounded-full uppercase tracking-wider text-right shadow-sm border border-primary/10">
                            {item['dept']}
                        </div>
                    </div>
                    <div class="text-primary opacity-[0.4] text-[48px] leading-[0.5] font-serif mb-2 font-bold select-none relative z-10">"</div>
                    <p class="text-white text-[14px] leading-[1.6] flex-grow text-left relative z-10">
                        {item['review']}
                    </p>
                    <div class="w-full h-px bg-primary/30 my-5 relative z-10"></div>
                    <div class="flex items-center gap-3 relative z-10">
                        <div class="size-10 rounded-full bg-primary flex items-center justify-center text-white font-bold text-[16px] shrink-0 shadow-sm border border-white/10 uppercase">
                            {item['name'][0]}
                        </div>
                        <div class="leading-tight text-left">
                            <h4 class="text-white font-bold text-[15px] mb-0.5">{item['name']}</h4>
                            <p class="text-slate-400 text-[12px]">{item['loc']}</p>
                        </div>
                    </div>
                </div>"""

def make_row(data):
    cards = "\n".join([make_card(i) for i in data])
    return f"""            <div class="flex gap-6 pr-6">
{cards}
            </div>
            <div class="flex gap-6 pr-6">
{cards}
            </div>"""

html = f"""    <!-- Patient Testimonials -->
    <section class="py-[100px] bg-navy-dark overflow-hidden relative border-t border-white/5">
        <style>
            @keyframes scroll-left {{
                from {{ transform: translateX(0); }}
                to {{ transform: translateX(-50%); }}
            }}
            @keyframes scroll-right {{
                from {{ transform: translateX(-50%); }}
                to {{ transform: translateX(0); }}
            }}
            .animate-scroll-left {{ animation: scroll-left 35s linear infinite; }}
            .animate-scroll-right {{ animation: scroll-right 35s linear infinite; }}
            
            /* Add group class locally for hover */
            .scroll-wrapper:hover .carousel-track {{
                animation-play-state: paused;
            }}
        </style>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 mb-16 text-center reveal-on-scroll">
            <span class="text-primary font-bold tracking-widest text-sm uppercase block mb-3">PATIENT STORIES</span>
            <h2 class="serif-heading text-[36px] text-white mb-4">What Our Patients Say</h2>
            <div class="w-16 h-1 bg-primary mx-auto mb-6 heading-underline"></div>
            <p class="text-slate-400 max-w-2xl mx-auto text-[16px]">
                Real experiences from real families across Upper Assam.
            </p>
        </div>

        <div class="relative w-full z-10 reveal-on-scroll translate-y-10" style="transition-delay: 0.1s;">
            <!-- Row 1 (RTL) -->
            <div class="scroll-wrapper w-full overflow-hidden mb-6">
                <div class="carousel-track flex w-max animate-scroll-left">
{make_row(data1)}
                </div>
            </div>

            <!-- Row 2 (LTR) -->
            <div class="scroll-wrapper w-full overflow-hidden px-12">
                <div class="carousel-track flex w-max animate-scroll-right">
{make_row(data2)}
                </div>
            </div>
        </div>

        <div class="mt-16 text-center relative z-10 reveal-on-scroll" style="transition-delay: 0.2s;">
            <p class="text-[#A0ADB8] text-[14px] mb-6">Join thousands of patients who trust Northeast Healthcare & Diagnostic with their health.</p>
            <button class="bg-primary hover:bg-[#239E8C] text-white px-8 py-3.5 rounded-lg font-bold transition-all shadow-md mt-2" onclick="document.getElementById('bookingModal').classList.remove('hidden')">
                Book Your Appointment Today
            </button>
        </div>
    </section>

    <!-- OT Complex -->"""

with open('C:\\Users\\chitr\\Downloads\\my websites\\Northeast healthcare & hospitals\\testim.txt', 'w', encoding='utf-8') as f:
    f.write(html)
