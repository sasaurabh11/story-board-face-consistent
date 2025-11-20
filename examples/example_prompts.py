fg_prompt = "a young Indian girl, 16-18 years old, with long black hair in a braid, wearing a cream-colored kurta with embroidered details, blue jeans, and a backpack, carrying books,"

bg_act_prompts = [
    dict(
        bg = "On a sunny street lined with buildings, trees, and a pathway leading toward a garden gate,",
        act = [
            "walking on the street, looking at the surroundings, curious expression, holding her backpack straps",
            "standing at the garden entrance, looking surprised and enchanted, front view",
        ],
    ),
    dict(
        bg = "Inside a lush green garden with colorful flowers, plants, and winding stone pathways,",
        act = [
            "walking through the garden, admiring the flowers, smiling with wonder, side view",
            "stopping to touch a blooming flower, delighted expression, bent forward slightly",
            "looking around the garden in awe, hands clasped together, front view",
        ],
    ),
    dict(
        bg = "At the hidden entrance to a small zoo, with ornate gates, tropical plants, and exotic bird sounds suggested in the background,",
        act = [
            "discovering the zoo entrance, eyes wide with surprise and excitement, front view",
            "standing at the zoo gate, peering inside with curiosity, side view",
        ],
        height=1280,
        width=720,
    ),
    dict(
        bg = "Inside the small zoo, surrounded by colorful animals - peacocks, deer, rabbits - with natural habitats and lush greenery,",
        act = [
            "observing peacocks displaying their feathers, amazed expression, front view",
            "gently approaching deer, careful and gentle movements, side view",
            "standing in the center of the zoo, looking around at all the animals, wonder-filled expression",
            "taking photos with her phone of the animals, focused and happy, side view",
        ],
    ),
    dict(
        bg = "In a tranquil zoo area with stone benches, flowering trees, and calm water features,",
        act = [
            "sitting on a bench, sketching the animals in her notebook, concentrated expression",
            "walking along a tree-lined path in the zoo, admiring the surroundings, peaceful expression",
        ],
        height=720,
        width=1280,
    ),
    dict(
        bg = "In an open zoo area with multiple enclosures, exotic animals visible in background, natural sunlight filtering through trees,",
        act = [
            "standing by an animal enclosure, observing animals closely, engaged expression, front view",
            "reading informational plaques about animals, educational pose, side view",
        ],
    ),
    dict(
        bg = "At sunset in the zoo, golden light filtering through trees, animals settling for evening,",
        act = [
            "sitting peacefully, reflecting on her exploration, serene expression",
            "taking a final look around the zoo before leaving, grateful and happy expression, back view",
        ],
    )
]